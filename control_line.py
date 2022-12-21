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
counter = -1
offset_distance = 0

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
  Regulator to follow right side.
  """
  refRight = 0.5
  err = refRight+lineRight
  w = K*err
  return v,w

def handleActions(msg):
  global actions
  global actionsList
  actions = msg
  #global actionsDict

  for index, action in enumerate(actions.actions): # Dobi akcije iz sporocila in sestavi list
    # actionsList = [smer, naslednja_tocka, razdalja]
    actionsList.append([action.action.id, action.action.name, action.action.distance]) 
  print(actionsList)

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
  global actionsList
  global counter 
  global offset_distance
  K = 3
  # Dictionary of tags: key is tag ID, value of 0 is folow left line, value of 1 is follow right line 
  # tagsDict = {20:0, 18:1, 8:0, 5:1, 1:1,9:1}
  # while len(actionsDict) == 0:
  #   pass
  
  #print(msg.line.left, msg.line.right)
  lineLeft = msg.line.left if not isnan(msg.line.left) else None
  lineRight = msg.line.right if not isnan(msg.line.right) else None
  distance = msg.line.distance if not isnan(msg.line.distance) else None

  #if not distance_set: 
    #offset_distance = distance
    #distance_set = True

  v=0
  w=0
  # 

  #print(f"Counter: {counter}")
  if counter == -1: # Prvic skozi akcije
    counter = 0
    offset_distance = distance
  #print(f"Len: {len(actionsList)}")
  if counter < len(actionsList): # Velikost stevca ne sme biti vecja od dolzine liste
    current_action = actionsList[counter] # Action to next node
    if current_action[0] >= 100: # Virtual tag
      distance_to_node = distance - offset_distance # Izracun razdalje    
      if distance_to_node >= current_action[2]: # Ce smo prevozili zahtevano razdaljo 
        counter +=1 # Pojdi na naslednjo akcijo
        offset_distance = distance 
    else: # Real tag
      if tag == current_action[0]: # Ce smo prevozili zahtevani tag
        counter +=1 # Pojdi na naslednjo akcijo
        offset_distance = distance 
      #if distance_to_node >= (current_action[2]*1.2): # Ce smo prevozili preveliko razdaljo
        #print("STOP: TAG NOT REACHED!")
        # TODO Kaj pa zdaj??
        # error = 1 # Preverjamo po vrstici 143 in damo v,w = 0 ??
    
    if lineLeft == None or lineRight == None: # Ce ne zaznavamo crte
      print("STOP: LINE NOT DETECTED!")
      v,w = 0,0
      # TODO Kaj pa zdaj??
    elif current_action[1] == "left":
      v,w = followLeft(K=K,lineLeft=lineLeft, v = 0.15) # Sledi levemu robu crte
    elif current_action[1] == "right":
      v,w = followRight(K=K,lineRight=lineRight, v = 0.15) # Sledi desnemu robu crte
    elif current_action[1] == "straight":
      v = 0.1
      w = 0
      # v,w = 0,0
      print("STRAIGHT: SPECIAL ACTION!")
      # TODO Kaj pa zdaj??
      # Glede na tag ID se odlocimo za ustrezno akcijo? voznja naravnost(18, 106, 108), voznja v tocko(132, 137) ??
    elif current_action[1] == 14 and tag == None :
      counter+=1
      offset_distance = distance
    else:
      v,w=0,0
      print("STOP: SPECIAL ACTION!")
    
    print(f"counter: {counter} | action to {current_action[0]} is {current_action[1]}")

    if counter == len(actionsList): # Prisli smo do konca liste
      v,w = 0,0
      print("STOP: GOAL REACHED!")
      # TODO Kaj pa zdaj??
      # counter = None # Priprava za novo pot??

  # v,w = 0
  # print("STOP")

  
  

  ##################################################################
  # #print(f"Line L: {lineLeft} | Line R: {lineRight}")
  # tagsDict = actionsDict
  
  # #v, w = 0.0, 0.0

  # # Follow left or right if tag is not in dictionary (left is 0, right is 1)
  # following = 1
  # if (following == 0 and lineLeft is None) or (following == 1 and lineRight is None): # Ce ne zaznavamo crte
  #   v = 0.0
  #   w = 0.0
  # elif tag in tagsDict:
  #   if tagsDict[tag] == 0:
  #     following = 0
  #   elif tagsDict[tag] == 1:
  #     following = 1

  # if following == 0:
  #   v,w = followLeft(K=K,lineLeft=lineLeft, v = 0.15)
  # elif following ==1:
  #   v,w = followRight(K=K,lineRight=lineRight, v = 0.15)
  #################################################################
  # print(tagsDict)
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
  
  print('New tag: {} -> {}'.format(msg.tag.id, tag))
  print(40*"-")



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