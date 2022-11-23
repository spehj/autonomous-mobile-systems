#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ams
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import sqrt, atan2, pi



# Handle odometry
def handleOdometry(msg):
  

  x,y,phi = ams.msgToPose(msg.pose.pose)
  gamma = msg.pose.pose.position.z

  error_d = 0
  alpha = 0
  beta = 0
  phi_err = 0
  phi_goal = 0
  x_goal = 0.40
  y_goal = 0.40
  d_robot = 0.1207
  r = 0.1
  Kv = 0.4
  Kw = 4.5
  Kg = 10

  phi_r = atan2(y_goal-y, x_goal-x)
  error_d = sqrt((x_goal-x)**2+(y_goal-y)**2)
  alpha = ams.wrapToPi(phi_r-phi_goal)
  beta = atan2(r,error_d)

  if alpha <0:
    beta = -beta
  
  if abs(alpha) <abs(beta):
    phi_err = ams.wrapToPi(phi_r-phi+alpha)
  else:
    phi_err = ams.wrapToPi(phi_r-phi+beta)

  


  

  if abs(phi_err) <= 2.5*0.00872664626 and abs(error_d) <= 0.01:
    ws = 0
    vs = 0
    print(msg)
  else:
    v = Kv*error_d
    w = Kw*(phi_err)
    vs = sqrt((d_robot*w)**2+v**2)
    if vs>0.3:
      vs=0.3

    gamma_goal = atan2(d_robot*w,v)
    ws = Kg*(gamma_goal-gamma)




  
  # 0, 1.5, -1.5,3
  # vs = 0.1
  # vs, ws = 0.0, 0.0

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
