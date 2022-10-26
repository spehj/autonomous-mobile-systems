#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph_gen import tagMap, tagDets

class PathPlanning(object):
  def __init__(self):
    pass

  def findPath(self, startId, goalId):
    '''Find the shortest path
    
    Inputs:
      startId - Id of the start tag.
      goalId  - Id of the goal tag.
            
    Outputs:
      path - A list of ordered tags that lead from the start tag to the goal tag
             (including start and goal tag) or an empty list if path is not found.
    '''
    path = []
    
    #TODO Implement path planning algorithm here ...
    
    return path

  def generateActions(self, path):
    '''Generate a list of actions for given path
    
    Inputs:
      path - A list of ordered tags that lead from the start tag to the goal tag
             (including start and goal tag) or an empty list if path is not found.

    Outputs:
      actions - A list of actions the AGV need to execute in order to reach the goal tag
                from the start tag or an empty list if no action is required/possible.
    '''
    actions = []

    #TODO Convert path to actions here ...
    #action = ('left', 20, 0.202)
    #actions.append(action)

    return actions



if __name__ == '__main__':
  pp = PathPlanning()
  path = pp.findPath(2, 12)
  print(path)
  actions = pp.generateActions(path)
  print(actions)
