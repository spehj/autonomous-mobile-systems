#!/usr/bin/python3
# -*- coding: utf-8 -*-

BOX = (0.0, 0.0, 2.2, 1.8)

EDGES = {
  '16-17': [('A', 0.650, 1.200, 0.075, 0.0, -90.0),
            ('A', 0.650, 1.050, 0.075, 90.0, 90.0)],
  '24-30': [('L', 0.425, 0.750, 0.425, 0.600),
            ('A', 0.500, 0.600, 0.075, -180.0, 90.0),
            ('A', 0.500, 0.450, 0.075, 90.0, -90.0)],
  '35-36': [('L', 0.800, 0.075, 1.100, 0.075)],
  '12-8':  [('B', 1.550, 1.275, 1.775, 1.275, 1.775, 1.575, 2.000, 1.575)],
  '25-27': [('A', 0.650, 0.750, 0.075, -180.0, 90.0),
            ('A', 0.650, 0.600, 0.075, 90.0, -90.0)],
  '26-33': [('L', 0.275, 0.600, 0.275, 0.300),
            ('A', 0.200, 0.300, 0.075, 0.0, -90.0),
            ('A', 0.200, 0.150, 0.075, 90.0, 90.0)],
  '10-33': [('L', 0.125, 1.350, 0.125, 0.150)],
  '41-5':  [('A', 1.100, 1.500, 0.075, 180.0, -90.0)],
  '21-22': [('L', 1.550, 0.825, 1.850, 0.825),
            ('A', 1.850, 0.750, 0.075, 90.0, -90.0)],
  '4-16':  [('A', 0.650, 1.500, 0.075, 90.0, -90.0),
            ('L', 0.725, 1.500, 0.725, 1.200)],
  '21-18': [('A', 1.550, 0.900, 0.075, -90.0, 90.0)],
  '34-35': [('L', 0.650, 0.075, 0.800, 0.075)],
  '31-28': [('A', 1.400, 0.450, 0.075, -90.0, -90.0),
            ('L', 1.325, 0.450, 1.325, 0.600)],
  '33-34': [('A', 0.200, 0.150, 0.075, -180.0, 90.0),
            ('L', 0.200, 0.075, 0.650, 0.075)],
  '17-25': [('L', 0.575, 1.050, 0.575, 0.750)],
  '15-1':  [('L', 2.075, 1.350, 2.075, 1.650)],
  '9-2':   [('A', 0.200, 1.500, 0.075, -180.0, 90.0),
            ('A', 0.200, 1.500, 0.075, -90.0, 90.0),
            ('A', 0.350, 1.500, 0.075, 180.0, -90.0)],
  '13-14': [('L', 1.700, 1.275, 2.000, 1.275)],
  '3-17':  [('A', 0.500, 1.500, 0.075, 90.0, -90.0),
            ('L', 0.575, 1.500, 0.575, 1.050)],
  '36-40': [('A', 1.100, 0.150, 0.075, -90.0, 90.0),
            ('L', 1.175, 0.150, 1.175, 0.300)],
  '2-24':  [('A', 0.350, 1.500, 0.075, 90.0, -90.0),
            ('L', 0.425, 1.500, 0.425, 0.750)],
  '6-7':   [('L', 1.325, 1.575, 1.550, 1.575)],
  '27-35': [('L', 0.725, 0.600, 0.725, 0.150),
            ('A', 0.800, 0.150, 0.075, -180.0, 90.0)],
  '38-23': [('L', 1.850, 0.075, 2.000, 0.075),
            ('A', 2.000, 0.150, 0.075, -90.0, 90.0),
            ('L', 2.075, 0.150, 2.075, 0.750)],
  '22-29': [('L', 1.925, 0.750, 1.925, 0.600)],
  '1-9':   [('A', 2.000, 1.650, 0.075, 0.0, 90.0),
            ('L', 2.000, 1.725, 0.200, 1.725),
            ('A', 0.200, 1.650, 0.075, 90.0, 90.0),
            ('L', 0.125, 1.650, 0.125, 1.500)],
  '2-3':   [('L', 0.350, 1.575, 0.500, 1.575)],
  '18-19': [('A', 1.700, 0.900, 0.075, 180.0, -90.0),
            ('L', 1.700, 0.975, 2.000, 0.975),
            ('A', 2.000, 1.050, 0.075, -90.0, 90.0)],
  '36-37': [('L', 1.100, 0.075, 1.400, 0.075)],
  '11-12': [('A', 1.400, 1.200, 0.075, 180.0, -90.0),
            ('L', 1.400, 1.275, 1.550, 1.275)],
  '25-30': [('L', 0.575, 0.750, 0.575, 0.450)],
  '10-26': [('A', 0.200, 1.350, 0.075, -180.0, 90.0),
            ('A', 0.200, 1.200, 0.075, 90.0, -90.0),
            ('L', 0.275, 1.200, 0.275, 0.600)],
  '24-26': [('A', 0.350, 0.750, 0.075, 0.0, -90.0),
            ('A', 0.350, 0.600, 0.075, 90.0, 90.0)],
  '7-14':  [('B', 1.550, 1.575, 1.775, 1.575, 1.775, 1.275, 2.000, 1.275)],
  '29-32': [('L', 1.925, 0.600, 1.925, 0.450),
            ('A', 1.850, 0.450, 0.075, 0.0, -90.0)],
  '32-31': [('L', 1.850, 0.375, 1.400, 0.375)],
  '5-6':   [('L', 1.100, 1.575, 1.325, 1.575)],
  '31-37': [('A', 1.400, 0.300, 0.075, 90.0, 90.0),
            ('L', 1.325, 0.300, 1.325, 0.150),
            ('A', 1.400, 0.150, 0.075, -180.0, 90.0)],
  '20-21': [('A', 1.400, 0.750, 0.075, 180.0, -90.0),
            ('L', 1.400, 0.825, 1.550, 0.825)],
  '31-39': [('L', 1.400, 0.375, 1.250, 0.375)],
  '23-19': [('L', 2.075, 0.750, 2.075, 1.050)],
  '14-15': [('A', 2.000, 1.350, 0.075, -90.0, 90.0)],
  '9-10':  [('L', 0.125, 1.500, 0.125, 1.350)],
  '22-23': [('A', 2.000, 0.750, 0.075, -180.0, 90.0),
            ('A', 2.000, 0.750, 0.075, -90.0, 90.0)],
  '28-20': [('L', 1.325, 0.600, 1.325, 0.750)],
  '30-34': [('L', 0.575, 0.450, 0.575, 0.150),
            ('A', 0.650, 0.150, 0.075, -180.0, 90.0)],
  '7-8':   [('L', 1.550, 1.575, 2.000, 1.575)],
  '4-5':   [('L', 0.650, 1.575, 1.100, 1.575)],
  '12-13': [('L', 1.550, 1.275, 1.700, 1.275)],
  '19-15': [('L', 2.075, 1.050, 2.075, 1.350)],
  '28-29': [('A', 1.400, 0.600, 0.075, 180.0, -90.0),
            ('L', 1.400, 0.675, 1.850, 0.675),
            ('A', 1.850, 0.600, 0.075, 90.0, -90.0)],
  '3-4':   [('L', 0.500, 1.575, 0.650, 1.575)],
  '16-27': [('L', 0.725, 1.200, 0.725, 0.600)],
  '37-38': [('L', 1.400, 0.075, 1.850, 0.075)],
  '20-11': [('L', 1.325, 0.750, 1.325, 1.200)],
  '11-6':  [('L', 1.325, 1.200, 1.325, 1.350),
            ('L', 1.325, 1.350, 1.250, 1.500),
            ('A', 1.325, 1.500, 0.075, 180.0, -90.0)],
  '18-13': [('L', 1.625, 0.900, 1.625, 1.200),
            ('A', 1.700, 1.200, 0.075, 180.0, -90.0)],
  '38-32': [('A', 1.850, 0.150, 0.075, -90.0, 90.0),
            ('L', 1.925, 0.150, 1.925, 0.300),
            ('A', 1.850, 0.300, 0.075, 0.0, 90.0)],
  '8-1':   [('A', 2.000, 1.650, 0.075, -90.0, 90.0)],
  '39-41': [('X', 1.250, 0.375, 1.181, 1.356),
            ('L', 1.181, 1.356, 1.025, 1.500)],
  '40-41': [('X', 1.175, 0.300, 0.867, 1.356),
            ('L', 0.867, 1.356, 1.025, 1.500)],
}

TAGS = {
#  # Real tags
#    1: (0.275, 1.725),
#    2: (0.200, 1.500),
#    3: (0.413, 1.575),
#    4: (0.552, 1.575),
#    5: (1.475, 1.567),
#    6: (0.725, 1.305),
#    7: (1.388, 1.224),
#    8: (1.325, 1.125),
#    9: (0.125, 0.847),
#   10: (0.275, 0.849),
#   11: (0.425, 0.855),
#   12: (0.575, 0.860),
#   13: (0.725, 0.852),
#   14: (1.475, 0.799),
#   15: (1.775, 0.825),
#   16: (1.338, 0.675),
#   17: (1.377, 0.463),
#   18: (1.504, 0.375),
#   19: (1.010, 0.075),
#   20: (1.752, 0.075),
   # Real tags
    1: (0.389, 1.720),
    2: (0.205, 1.494),
    3: (0.348, 1.570),
    4: (0.490, 1.574),
    5: (1.373, 1.574),
    6: (0.706, 1.398),
    7: (1.375, 1.215),
    8: (1.324, 0.999),
    9: (0.124, 0.949),
   10: (0.275, 0.955),
   11: (0.425, 0.958),
   12: (0.575, 0.960),
   13: (0.725, 0.953),
   14: (1.380, 0.772),
   15: (1.711, 0.822),
   16: (1.327, 0.639),
#   16: (1.333, 0.576), # Alternative tag
   17: (1.368, 0.433),
   18: (1.613, 0.373),
   19: (0.947, 0.075),
#   19: (0.856, 0.085), # Alternative tag
   20: (1.627, 0.075),
#   20: (1.486, 0.078), # Alternative tag
  # Virtual tags
  101: (0.856, 1.575),
  102: (1.156, 1.575),
  103: (1.776, 1.575),
  104: (2.000, 1.575),
  105: (1.025, 1.510),
  106: (1.722, 1.490),
  107: (1.825, 1.489),
  108: (1.723, 1.361),
  109: (1.824, 1.362),
  110: (2.075, 1.446),
  111: (0.125, 1.406),
  112: (0.575, 1.331),
  113: (1.325, 1.331),
  114: (1.628, 1.275),
  115: (1.786, 1.275),
  116: (2.006, 1.275),
  117: (0.650, 1.122),
  118: (2.075, 1.136),
  119: (1.624, 1.050),
  120: (1.831, 0.975),
  121: (1.606, 0.852),
  122: (2.075, 0.817),
  123: (1.925, 0.694),
  124: (2.000, 0.674),
  125: (1.644, 0.675),
  126: (0.350, 0.674),
  127: (0.650, 0.675),
  128: (0.575, 0.619),
  129: (0.500, 0.526),
  130: (1.925, 0.506),
  131: (0.275, 0.431),
  132: (1.306, 0.375),
  133: (2.075, 0.319),
  134: (1.325, 0.281),
  135: (0.575, 0.281),
  136: (0.725, 0.284),
  137: (1.175, 0.244),
  138: (1.925, 0.169),
  139: (0.331, 0.075),
  140: (0.669, 0.075),
  141: (1.231, 0.075),
  142: (0.920, 1.400),
  143: (1.130, 1.400),
}

NODES = {
   1: (2.075, 1.650),
   2: (0.350, 1.575),
   3: (0.500, 1.575),
   4: (0.650, 1.575),
   5: (1.100, 1.575),
   6: (1.325, 1.575),
   7: (1.550, 1.575),
   8: (2.000, 1.575),
   9: (0.125, 1.500),
  10: (0.125, 1.350),
  11: (1.325, 1.200),
  12: (1.550, 1.275),
  13: (1.700, 1.275),
  14: (2.000, 1.275),
  15: (2.075, 1.350),
  16: (0.725, 1.200),
  17: (0.575, 1.050),
  18: (1.625, 0.900),
  19: (2.075, 1.050),
  20: (1.325, 0.750),
  21: (1.550, 0.825),
  22: (1.925, 0.750),
  23: (2.075, 0.750),
  24: (0.425, 0.750),
  25: (0.575, 0.750),
  26: (0.275, 0.600),
  27: (0.725, 0.600),
  28: (1.325, 0.600),
  29: (1.925, 0.600),
  30: (0.575, 0.450),
  31: (1.400, 0.375),
  32: (1.850, 0.375),
  33: (0.125, 0.150),
  34: (0.650, 0.075),
  35: (0.800, 0.075),
  36: (1.100, 0.075),
  37: (1.400, 0.075),
  38: (1.850, 0.075),
  39: (1.250, 0.375),
  40: (1.175, 0.300),
  41: (1.025, 1.500),
}

MTAG = {
  584190835274: 1,
  584191425717: 2,
  584190573134: 3,
  584191294388: 4,
  584190048838: 5,
  584190310978: 6,
  584191556528: 7,
  584189523795: 8,
  584184871702: 9,
  584184609578: 10,
  584184347438: 11,
  584184085282: 12,
  584183823142: 13,
  584189785943: 14,
  584189326943: 15,
  584183561018: 16, #584185199377 # Alternative tag
  584182905652: 17,
  584199420872: 18,
  584194635661: 19, #584189786714 # Alternative tag
  584191687865: 20 #584194307978 (not detected) or 584191687865 (alternative tag)
}

SPACES = [((0.797,         0.225+1.135),
           (0.797,         0.225),
           (0.797+0.454,   0.225),
           (0.797+0.454,   0.225+1.135),
           (0.797+0.454/2, 0.225+1.135+0.216))]
