#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ams
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import sqrt, atan2



# Handle odometry
def handleOdometry(msg):
  print(msg)

  x,y,phi = ams.msgToPose(msg.pose.pose)
  gamma = msg.pose.pose.position.z

  phi_ref = 0
  x_ref = 0.40
  y_ref = 0.40
  d_robot = 0.1207
  K1 = 2
  K2 = 2
  K3 = 5


  v = K1*sqrt((x_ref-x)**2+(y_ref-y)**2)
  w = K2*(phi_ref-phi)
  vs = sqrt((d_robot*w)**2+v**2)
  gamma_ref = atan2(d_robot*w,v)
  ws = K3(gamma_ref-gamma)


  
  
  #vs, ws = 0.0, 0.0

  # Velocity commands message
  msgCmdVel = Twist()
  msgCmdVel.linear.x = vs
  msgCmdVel.angular.z = ws
  # Publish velocity commands
  pubCmdVel.publish(msgCmdVel)



try:
  rospy.init_node('control_line')
  
  # Velocity commands publisher.
  pubCmdVel = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  # Odometry subscriber
  subOdom = rospy.Subscriber('odom', Odometry, handleOdometry)

  rospy.spin()
except KeyboardInterrupt:
    pass
