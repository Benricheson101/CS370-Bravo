
# In the Kroz pascal code, every "row" of a level is story in an array
# Level text data stored in a list by row
# level_data dimensions: 23 x 64
level_data = [
    "+ + + + ס               #temple#of#kroz#   1      XX ]-5--****-%",
    " + + + +#]   ]        1 #######by#######          XX  ]5--*TT*--",
    "+ + + +%#  1        XX  ##scott#miller##         1    -5--****--",
    "#########           XX                                -555555555",
    "&;                             XX    1                ]-------]-",
    ";;            XX    1          XX          XX    ]        ]   1 ",
    "    XX    1   XX    ]        ]             XX        1   XX     ",
    "    XX                             XX  ]                 XX     ",
    "]           ]         ]            XX      1                   ]",
    "      1                        ]                    ]        1  ",
    "           XX                !     *            XX              ",
    "           XX        XX         P     ]         XX              ",
    "XX     ]         ]   XX      T     S                           1",
    "XX  1                                       ]          XX   ]   ",
    "             1            ]             XX       1     XX     XX",
    "]]]]]]]]]                    XX        XX                    XX",
    "XXXXXXXXX]  ]     XX          XX   ]                ]   1       ",
    "XXXXXXXXX]        XX              1                        ]   1",
    "XXXXXXXXX]             1                     1       ]----------",
    "XXXXXXXXX]    1          XX   ]                   XX  -444444444",
    "XXXXXXXXX]  XX           XX              ]        XX ]-4WעWעWעWע",
    "]]XXXXXXX]  XX ]           ]    XX   1                -4עWעWעWעW",
    "L&XXXXXXX]    1     1           XX               1   ]-4WעWעWעW%",
]


# gets the position of a given text character in the level_data list
def get_entity_pos(list, entity):
    indexes = []
    for i, row in enumerate(list):
        for j, value in enumerate(row):
            if value == entity:
                indexes.append((j, i))
    return indexes


wall_pos = get_entity_pos(level_data, "X")
gem_pos = get_entity_pos(level_data, "+")
player_pos = get_entity_pos(level_data, "P")
