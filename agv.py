#!/usr/bin/python3
# -*- coding: utf-8 -*-
from matplotlib.transforms import offset_copy
import ams
from agvapi import Agv, findLineEdges
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from amsagv_msgs.msg import LineStamped
from math import cos, sin, pi

global distance

with Agv() as robot:
  # Handle velocity commands
  def handleCmdVel(msg):
    global robot
    robot.setVel(msg.linear.x, msg.angular.z)



  try:
    rospy.init_node('agv')
    ns = rospy.get_namespace().lstrip('/')
    # Name of the odometry frame
    paramOdomFrameId = rospy.get_param('~odom_frame_id', '{}odom'.format(ns))
    # Name of the AGV frame
    paramAgvFrameId = rospy.get_param('~agv_frame_id', '{}agv'.format(ns))

    # Odometry publisher
    pubOdom = rospy.Publisher('odom', Odometry, queue_size=1)
    # Line sensor publisher
    pubLine = rospy.Publisher('line', LineStamped, queue_size=1)
    # Velocity commands subscriber.
    subCmdVel = rospy.Subscriber('cmd_vel', Twist, handleCmdVel)

    # Line-sensor message
    msgLine = LineStamped()

    # Odometry message
    msgOdom = Odometry()
    msgOdom.header.frame_id = paramOdomFrameId
    msgOdom.child_frame_id = paramAgvFrameId

    # Odometry initial state
    x, y, phi, gamma = 0.0, 0.0, 0.0, 0.0 # Robot configuration
    # fd = 0.0 # Travelled distance of the front cart

    rate = rospy.Rate(50)
    isFirst = True
    pulsePerM = 111.5*1000 # pulzov na m
    deltaLeftPulse = 0
    deltaRightPulse = 0
    lastRightPulse = 0
    lastLeftPulse = 0
    sLeft = 0
    sRight = 0
    pulseConst = float(1/pulsePerM)
    vLeft = 0
    vRight = 0
    vSpeed = 0
    d_robot = 0.1207
    l_robot = 0.043
    #path_distance = 0 # Path of fron axis
    distance = 0
    while not rospy.is_shutdown():
      t = rospy.Time.now()

      # Read sensors
      robot.readSensors()

      # Encoders
      encLeft, encRight, encHeading = robot.getEncoders()

    
      gamma = (-1)*ams.wrapToPi(((encHeading+2475)*2*pi)/(8192)) # encHeading-2568
      if isFirst:
        # Just read
        lastLeftPulse= encLeft        
        lastRightPulse = encRight
        x = 0
        y = 0
        phi = 0
        isFirst = False
      elif not isFirst:
        # Read and move
        deltaLeftPulse = encLeft - lastLeftPulse 
        deltaRightPulse = encRight-lastRightPulse

        sLeft = pulseConst*deltaLeftPulse
        sRight = pulseConst*deltaRightPulse

        vLeft = deltaLeftPulse/pulsePerM #sLeft/deltaTime
        vRight = deltaRightPulse/pulsePerM #sRight/deltaTime
        vSpeed = (-vLeft+vRight)/2.0

        distance += vSpeed
        
        # delta_gama = (vRight-vLeft)/l_robot
        x += vSpeed*cos(gamma)*cos(phi)
        y += vSpeed*cos(gamma)*sin(phi)
        phi +=(vSpeed*sin(gamma))/(d_robot)
        
      lastLeftPulse = encLeft
      lastRightPulse = encRight      

      # Odometry message
      
      msgOdom.header.stamp = t
      msgOdom.pose.pose = ams.poseToPoseMsg(x, y, phi)
      msgOdom.pose.pose.position.z = gamma
      msgOdom.twist.twist.linear.x = vSpeed
      # Publish odometry message
      pubOdom.publish(msgOdom)
      
      # Line sensor

      # Line-sensor values
      lineValues = robot.getLineValues()
      # Left and right line edge
      edgeLeft, edgeRight = findLineEdges(lineValues)

      # Line-sensor message
      msgLine.header.stamp = t
      msgLine.line.values = lineValues
      msgLine.line.left = edgeLeft if edgeLeft is not None else float('nan')
      msgLine.line.right = edgeRight if edgeRight is not None else float('nan')
      msgLine.line.heading = gamma
      msgLine.line.distance = distance
      # Publish line-sensor message
      pubLine.publish(msgLine)

      rate.sleep()
  except KeyboardInterrupt:
    pass
