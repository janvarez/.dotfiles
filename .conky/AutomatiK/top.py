# -*- encoding: utf-8 -*-
import os
header = open('header.py', 'r').read()
from translations import *
from useful_modules import *
Language=detect_language()


txt01="""gap_x = 350,
	gap_y = 50,

};

conky.text = [[
${image icons/gearwheels.png -p 0,0 -s 30x30}
${offset 35}${font Good Times:size=12}${color Tan1}"""+TasksProcesses[Language]+""" ${color}${hr 2}${font}
${offset 5}${color}"""+Load[Language]+""" ${loadavg 1}
#${running_processes} ${running_threads} ${processes}
${hr 2}${font}
${color lightgrey}${font Futurist Fixed-width:size=10:bold}${color lightgrey}${offset 5}PROCESS          CPU${alignr}   """+Memory[Language]+"""        ${offset -5}PID
${voffset -10}${hr 1}${font}${color}${font monofur:size=11}
${voffset -5}#
${offset 5}${top name 1} ${alignr}${top cpu 1}%      ${top mem_res 1}     ${alignr}${offset -5}${top pid 1}
${offset 5}${top name 2} ${alignr}${top cpu 2}%      ${top mem_res 2}     ${alignr}${offset -5}${top pid 2}
${offset 5}${top name 3} ${alignr}${top cpu 3}%      ${top mem_res 3}     ${alignr}${offset -5}${top pid 3}
${offset 5}${top name 4} ${alignr}${top cpu 4}%      ${top mem_res 4}     ${alignr}${offset -5}${top pid 4}
${offset 5}${top name 5} ${alignr}${top cpu 5}%      ${top mem_res 5}     ${alignr}${offset -5}${top pid 5}]];"""
# ${offset 5}${image img/proc-box01.png -p 0,48 -s 320x115}
# ${top name 1} $alignr ${top mem 1} ${tab 10} ${top cpu 1} ${top pid 1}

total=header+txt01
#print total

Write_File('topfile',total)
