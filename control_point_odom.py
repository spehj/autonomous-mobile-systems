#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ams
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry



# Handle odometry
def handleOdometry(msg):
  print(msg)
  
  vs, ws = 0.0, 0.0

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
