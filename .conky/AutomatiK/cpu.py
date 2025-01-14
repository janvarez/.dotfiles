# -*- encoding: utf-8 -*-
import os
import platform
header = open('header.py', 'r').read()
from useful_modules import *
from translations import *
Language=detect_language()

# ---------------------------------
# determine what is the best sensor
# ---------------------------------

#  sed -e 's/([^()]*)//g'  enleve les parantheses
# grep -Eo '[0-9]{1,13}' pour ne récupérer que les chiffres
# sed -n -e 's/^.*+//p' ne recupére que ce qui'il y a après + signe +
# test with Core - INTEL
TemperatureSensor="sensors | grep -E 'Package id 0|Physical id 0|Tctl|temp1' | sed -e 's/([^()]*)//g' |  grep -oP '\+(\d+\.\d+)°C' | sort -n | tail -n 1"
#                            only get temp1 Code Tctl   last match remove between ()   

# determine installed language
#Language_installed=os.popen("locale | grep LANG").read()
#print Language_installed

# number of cores
NumberOfCores=os.popen("cat /proc/cpuinfo | grep proc | wc -l").read()
#NumberOfCores=12
# print NumberOfCores

CpuInf=os.popen("echo `grep -m1 'model name' /proc/cpuinfo| sed -n '/: /s/.............//p'`").read().replace("	", " ")
# print CpuInf



DistroID=os.popen("lsb_release -si | tr '[:upper:]' '[:lower:]'").read()
if "raspbian" in DistroID:
	txt01="""gap_x = 15,
	gap_y = 492,

	lua_load = 'allcombined.lua',


};

conky.text = [[
${image img/cpu2.png -p 0,0 -s 30x30}
${offset 35}${font AvantGardeLTMedium:size=14}${color Tan1}"""+CpuInformation[Language]+""" ${color}${hr 2}
${font}${color}${execi 1000 cat /proc/cpuinfo | grep 'model name' | sed -e 's/model name.*: //'| uniq}
${color lightgrey}"""+Temperature[Language]+""" ${texeci 10 echo $((`cat /sys/class/thermal/thermal_zone0/temp`/1000))°C}
${alignc}${color #000000}${cpugraph 20,318 000000 FFEF00}"
"""
else:

	txt01="""gap_x = 15,
	gap_y = 492,

	lua_load = 'allcombined.lua',


};

conky.text = [[
${image icons/cpu2.png -p 0,0 -s 30x30}
${offset 35}${font Good Times:size=12}${color Tan1}"""+CpuInformation[Language]+""" ${color}${hr 2}
${font}${color}${execi 1000 cat /proc/cpuinfo | grep 'model name' | sed -e 's/model name.*: //'| uniq}
${color lightgrey}"""+Temperature[Language]+""": ${alignr}${texeci 10 """+TemperatureSensor+"""}
${alignc}${color #000000}${cpugraph 20,318 000000 FFFFFF}${color}
"""

List = []
Height=110
#NumberOfCores=1
for Cores in range(int(NumberOfCores)):
    Comment="# CPU"+str(Cores+1)+"\n"
    CpuName=""+Cpu[Language]+" "+str(Cores+1)
    CpuUsage="${goto 50} : ${cpu cpu"+str(Cores+1)+"}%"
    CpuGraph=' ${lua gradbar {100, '+str(Height)+', "${cpu cpu'+str(Cores+1)+'}", 100, 40, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}'
    CpuFrequency="${goto 230}${color}${freq "+str(Cores+1)+"} MHz"
    BackgroundImage="${image img/trans-bg240.png -p 96,"+str(Height-5)+" -s 121x11}"+"\n"

    List.append(Comment)
    List.append(CpuName)
    List.append(CpuUsage)
    List.append(CpuGraph)
    List.append(CpuFrequency)
    List.append(BackgroundImage)

	
	
    Height=Height+15
TotalCpu=''.join(List)
total=header+txt01+TotalCpu + "]];"
#print (total)


Write_File('cpufile',total)
