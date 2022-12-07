#!/usr/bin/python3
# -*- coding: utf-8 -*-
from graph_gen import tagMap, tagDets
from math import sqrt

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
    path = []
    open_list = []
    close_list = []

    #h = 0 # Dijkstra
    h = sqrt((tagDets[startId][0] - tagDets[goalId][0])**2 + (tagDets[startId][1] - tagDets[goalId][1])**2) # Heuristika med zacetkom in ciljem

    #open_list = [[tockaID, cena_do_sem, cena_do_cilja, skupna_cena, starsID],[tocka1],[tocka2],...]
    open_list = [[startId,0,h,h,None]] # Startno tocko v open listo

    while len(open_list) > 0: # Dokler imamo tocke v open_list, drugace pot ni najdena
      open_list.sort(key = lambda x:x[3]) # Sortiramo open_list po velikosti glede na skupna_cena
      activeId = open_list[0][0] # Prvi element ima najmanjso skupna_cena
      activeId_g = open_list[0][1] # g od trenutne tocke

      on_close_list = 0
      for j in range(len(close_list)): # Pojdi cez listo
        if close_list[j][0] == activeId: # Dobi index kje v listi se nahaja tocka 
          on_close_list = 1 # Tocka je ze na close_list
      if on_close_list == 0: # Ce tocka se ni na close_list 
        close_list.append(open_list[0]) # Dodaj ga v close_list
      open_list.pop(0) # Odstrani iz open_list

      if activeId == goalId: # Ce smo prisli do ciljne tocke se ustavimo
        #print("Path found!")
        parent = activeId
        path.append(parent) # Dodaj zadnjo/ciljno tocko
        while parent != startId: # Nazaj po poti do prve tocke
          for i in range(len(close_list)): # Pojdi cez listo
            if close_list[i][0] == parent: # Dobi index kje v listi se nahaja tocka
              parent = close_list[i][4] # Dobi starsa te tocke
              path.append(parent) # Dodaj starsa
        path.reverse() # Obrni vrstni red poti
        break # Izhod iz zanke 

      n = len(tagMap[activeId]) # Dobi stevilo sosednjih tock (in dolzin)
      for i in range(n): # Pojdi cez elemente trenutne tocke
        if i % 2 == 0: # Neparno oz. IDji sosednjih tock
          neighbourId = tagMap[activeId][i] # Dobi IDje sosednjih tock
          if neighbourId != 0: # ID ne sme biti 0 ker v tem primeru leva/desna sosednja tocka ne obstaja
            on_open_list = 0
            for j in range(len(open_list)): # Pojdi cez listo
              if open_list[j][0] == neighbourId: # Dobi index kje v listi se nahaja tocka
                on_open_list = j # Tocka je ze na open_list in to je index
            g = tagMap[activeId][i+1] + activeId_g # Razdalja od trenutne do sosednje tocke + vsota prejsnih razdalj med tockami
            #h = 0 # Dijkstra
            h = sqrt((tagDets[neighbourId][0] - tagDets[goalId][0])**2 + (tagDets[neighbourId][1] - tagDets[goalId][1])**2) 
            f = g + h
            if on_open_list > 0 and f < open_list[on_open_list][3]: # Ce je tocka ze na open_list in je nova razdalja manjsa
              open_list[on_open_list][1] = g # Posodobi g
              open_list[on_open_list][2] = h # Posodobi h
              open_list[on_open_list][3] = f # Posodobi f
              open_list[on_open_list][4] = activeId # Posodobi starsa
            if on_open_list == 0: # Ce tocka se ni na open_list
              open_list.append([neighbourId,g,h,f,activeId]) # Dodaj v open_list

    #print(len(open_list))
    #print(open_list)
    #print(close_list)
    #print(len(close_list))

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
    # actions = [smer, naslednja_tocka, razdalja]
    actions = []

    #TODO Convert path to actions here ...
    for i in range(len(path)-1): # Pojdi cez pot
      distance = 0
      activeId = path[i] # Trenutna tocka
      nextId = path[i+1] # Naslednja tocka
      for j in range(len(tagMap[activeId])): # Pojdi cez elemente trenutne tocke
        if tagMap[activeId][j] == nextId: # Najdi index naslednje tocke
          distance = tagMap[activeId][j+1] # Razdalja do naslednje tocke
          if j == 0: # Index desne tocke = 0
            direction = 'left'
          elif j == 2: # Index leve tocke = 2
            direction = 'right'
          else: # Index naravnost tocke = 4
            direction = 'straight'
      actions.append([direction, nextId, distance])

    return actions



if __name__ == '__main__':
  pp = PathPlanning()
  #path = pp.findPath(16, 1) 
  path = pp.findPath(2, 12)
  print(path)
  actions = pp.generateActions(path)
  print(actions)