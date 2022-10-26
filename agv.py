#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ams
from agvapi import Agv, findLineEdges
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from amsagv_msgs.msg import LineStamped



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
    fd = 0.0 # Travelled distance of the front cart

    rate = rospy.Rate(50)
    isFirst = True
    pulzPermm = 111.5 # pulzov na mm
    deltaLeftPulse = 0
    deltaRightPulse = 0
    lastRightPulse = 0
    lastLeftPulse = 0
    sLeft = 0
    sRight = 0
    pulseConst = 1/pulzPermm
    vLeft = 0
    vRight = 0
    lastTime = 0
    vSpeed = 0
    d_robot = 0.1207
    l_robot = 0.043
    while not rospy.is_shutdown():
      t = rospy.Time.now()

      # Read sensors
      robot.readSensors()

      #
      # Odometry
      #

      # Encoders
      encLeft, encRight, encHeading = robot.getEncoders()

      #TODO Implement odometry here ...
      print('Encoders: left={}, right={}, heading={}'.format(encLeft, encRight, encHeading))

      if isFirst:
        # Just read
        lastLeftPulse= encLeft
        lastRightPulse = encRight
        # TODO add heading
        isFirst = False
      elif not isFirst:
        # Read and move
        deltaTime = t-lastTime
        deltaLeftPulse = encLeft - lastLeftPulse 
        deltaRightPulse = encRight-lastRightPulse
        sLeft = pulseConst*deltaLeftPulse
        sRight = pulseConst*deltaRightPulse

        vLeft = sLeft/deltaTime
        vRight = sRight/deltaTime
        vSpeed = (vLeft+vRight)/2

        delta_gama = (vRight-vLeft)/l_robot
        

      
      
      
      
      lastTime = t



      # Odometry message
      msgOdom.header.stamp = t
      msgOdom.pose.pose = ams.poseToPoseMsg(x, y, phi)
      # Publish odometry message
      pubOdom.publish(msgOdom)

      #
      # Line sensor
      #

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
      msgLine.line.distance = fd
      # Publish line-sensor message
      pubLine.publish(msgLine)

      rate.sleep()
  except KeyboardInterrupt:
    pass
