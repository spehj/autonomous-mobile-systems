#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ams
import rospy
from geometry_msgs.msg import Twist
from amsagv_msgs.msg import LineStamped, TagStamped
from math import pi, sin, cos, isnan
from world import MTAG
from amsagv_msgs.msg import ActionsStamped


actions = None
tag = None
actionsDict = {}
actionsList = []
def followLeft(K, lineLeft, v):
  """
  Regulator to follow left side.
  """
  refLeft = -0.3
  err = refLeft+lineLeft
  w = K*err
  return v,w

def followRight(K, lineRight, v):
  """
  Regulator to follow left side.
  """
  refRight = 0.5
  err = refRight+lineRight
  w = K*err
  return v,w

def handleActions(msg):
  global actions
  global actionsList
  actions = msg
  global actionsDict

  for index, action in enumerate(actions.actions):
    actionsList[index] = [action.action.id, action.action.name]
    if action.action.name == "right":
      actionsDict[action.action.id] = 1
    elif action.action.name == "left":
      actionsDict[action.action.id] = 0
  #print(action.action.name)
  print(actionsDict)

# def getPath(msg):
#   # actions: 
#   # - 
#   #   header: 
#   #     seq: 0
#   #     stamp: 
#   #       secs: 0
#   #       nsecs:         0
#   #     frame_id: ''
#   #   action: 
#   #     name: "right"
#   #     id: 111
#   #     distance: 0.4869999885559082
#   # - 
#   #   header: 
#   #     seq: 0
#   #     stamp: 
#   #       secs: 0
#   #       nsecs:         0
#   #     frame_id: ''
#   #   action: 
#   #     name: "right"
#   #     id: 9
#   #     distance: 0.5199999809265137
#   # - 
#   #   header: 
#   #     seq: 0
#   #     stamp: 
#   #       secs: 0
#   #       nsecs:         0
#   #     frame_id: ''
#   #   action: 
#   #     name: "right"
#   #     id: 139
#   #     distance: 0.9850000143051147


# Handle line sensor
def handleLine(msg):
  global actionsDict
  K = 3
  # Dictionary of tags: key is tag ID, value of 0 is folow left line, value of 1 is follow right line 
  # tagsDict = {20:0, 18:1, 8:0, 5:1, 1:1,9:1}
  # while len(actionsDict) == 0:
  #   pass
  tagsDict = actionsDict
  #print(msg.line.left, msg.line.right)
  lineLeft = msg.line.left if not isnan(msg.line.left) else None
  lineRight = msg.line.right if not isnan(msg.line.right) else None

  #print(f"Line L: {lineLeft} | Line R: {lineRight}")
  
  #v, w = 0.0, 0.0

  # Follow left or right if tag is not in dictionary (left is 0, right is 1)
  following = 1
  if (following == 0 and lineLeft is None) or (following == 1 and lineRight is None): # Ce ne zaznavamo crte
    v = 0.0
    w = 0.0
  elif tag in tagsDict:
    if tagsDict[tag] == 0:
      following = 0
    elif tagsDict[tag] == 1:
      following = 1

  if following == 0:
    v,w = followLeft(K=K,lineLeft=lineLeft, v = 0.15)
  elif following ==1:
    v,w = followRight(K=K,lineRight=lineRight, v = 0.15)

  print(tagsDict)
  #print(f"w: {w}")
  # Velocity commands message
  msgCmdVel = Twist()
  msgCmdVel.linear.x = v
  msgCmdVel.angular.z = w
  # Publish velocity commands
  pubCmdVel.publish(msgCmdVel)



def handleTag(msg):
  global tag
  tag = MTAG.get(msg.tag.id, None)
  
  #print('New tag: {} -> {}'.format(msg.tag.id, tag))
  #print(40*"-")



try:
  rospy.init_node('control_line')
  
  # Velocity commands publisher.
  pubCmdVel = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  # Line sensor subscriber
  subLine = rospy.Subscriber('line', LineStamped, handleLine)
  # Tag subscriber
  subTag = rospy.Subscriber('tag', TagStamped, handleTag)
  # Action subscriber
  rospy.Subscriber('path_actions', ActionsStamped, handleActions)

  rospy.spin()
except KeyboardInterrupt:
  pass
