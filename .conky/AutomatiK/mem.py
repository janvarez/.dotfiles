# -*- encoding: utf-8 -*-
import os
header = open('header.py', 'r').read()
from translations import *
from useful_modules import *
Language=detect_language()









txt01="""
	gap_x = 15,
	gap_y = 343,
	lua_load = 'allcombined.lua',

--${lua gradbar {5, 218 "${memperc}" ,100, 80, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}

};
conky.text = [[
${image img/memory.png -p 0,0 -s 30x30}
${offset 35}${font Good Times:size=12}${color Tan1}"""+Memory[Language]+""" ${color}${hr 2}${font}
${color}"""+Ram[Language]+"""${color}${alignr}$memmax 
${lua gradbar {6, 55, "${memperc}", 100, 97, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}
${color}$mem """+UsedWord[Language]+"""${alignr}${memfree} """+FreeWord[Language]+"""
${image img/trans-bg240.png -p 2,50 -s 290x11}
${color}"""+Swap[Language]+"""${alignr}${swapmax}
${lua gradbar {6, 115 ,"${swapperc}", 100, 97, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}
${color}$swap """+UsedWord[Language]+"""${alignr}${swapfree} """+FreeWord[Language]+"""
${image img/trans-bg240.png -p 2,110 -s 290x11}#
]];
"""


total=header+txt01
#print total

Write_File('memfile',total)
