#!/usr/bin/python3
# -*- coding: utf-8 -*-
from math import *
import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from amsagv_msgs.msg import TagStamped
#import numpy as np
#from ams import wrapToPi
#from world import MTAG
#import graph_gen as graph
#import tf.transformations as tft



class Localisation(object):
  def __init__(self):
    self._tfBroadcaster = tf2_ros.TransformBroadcaster()

    # Odometry subscriber
    self._subOdom = rospy.Subscriber('odom', Odometry, self._handleOdometry)
    # Tag subscriber
    self._subTag = rospy.Subscriber('tag', TagStamped, self._handleTag)

    self.x, self.y, self.phi = 0.0, 0.0, 0.0

  def _handleTag(self, msg):
    print('Tag ID: {}'.format(msg.tag.id))

  def _handleOdometry(self, msg):
    #TODO Implement localisation algorithm here ...

    #'''
    trans = TransformStamped()
    trans.header.stamp = rospy.Time.now()
    trans.header.frame_id = 'world'
    trans.child_frame_id = 'NS/estimate'
    trans.transform.translation.x = self.x
    trans.transform.translation.y = self.y
    trans.transform.rotation.z = sin(self.phi/2.0)
    trans.transform.rotation.w = cos(self.phi/2.0)
    self._tfBroadcaster.sendTransform(trans)
    '''
    vecTodom2agv = np.array([msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z])
    vecQodom2agv = np.array([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])
    vecTworld2agv = np.array([self.x, self.y, 0.0])
    vecQworld2agv = np.array([0.0, 0.0, sin(self.phi/2.0), cos(self.phi/2.0)])
    vecQworld2odom = tft.quaternion_multiply(vecQworld2agv, tft.quaternion_conjugate(vecQodom2agv))
    matRworld2odom = tft.quaternion_matrix(vecQworld2odom)[0:3,0:3]
    vecTworld2odom = vecTworld2agv - matRworld2odom.dot(vecTodom2agv)
    msgQworld2odom = Quaternion(*vecQworld2odom)
    msgTworld2odom = Point(*vecTworld2odom)

    trans2 = TransformStamped()
    trans2.header.stamp = msg.header.stamp
    trans2.header.frame_id = 'world'
    trans2.child_frame_id = 'NS/odom'
    trans2.transform.translation = msgTworld2odom
    trans2.transform.rotation = msgQworld2odom

    transMsg = TransformStamped()
    transMsg.header = msg.header
    transMsg.child_frame_id = msg.child_frame_id
    transMsg.transform.translation = msg.pose.pose.position
    transMsg.transform.rotation = msg.pose.pose.orientation

    self._tfBroadcaster.sendTransform([trans2, transMsg])
    #'''



if __name__ == '__main__':
  try:
    rospy.init_node('localisation')

    localisation = Localisation()

    rospy.spin()
  except KeyboardInterrupt:
    pass
