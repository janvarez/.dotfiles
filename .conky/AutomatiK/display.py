# -*- encoding: utf-8 -*-
import os
import sys
from nvidia import Middle_text
from useful_modules import *
from translations import *
Language=detect_language()



#####################################################
##
##         Inxi output
##
#####################################################

Total=os.popen("inxi -aG -y1").read().split('\n')
#Total = DEBUGSTR.split('\n')
Total_Clean=[]
for line in Total:
	clean_line=line
	Total_Clean.append(clean_line)






"""
try:
	os.popen("rm graphiccardfile").read().split('\n')
except:
	pass
"""


#####################################################
##
##         Load header of conky file
##
#####################################################

header = open('header.py', 'r').read()


########################################################################
##
##                          X11 or wayland ?
##
########################################################################
Graphic_server_installed = Inxi_Search("Display:",Total_Clean)[0]


########################################################################
##
##                          find the GPU card
##
########################################################################
GPU_NAME_Device1 = Inxi_Search("Device-1",Total_Clean)[0]
GPU_NAME_Renderer = Inxi_Search("renderer:",Total_Clean)[0]
if len(GPU_NAME_Device1) > len(GPU_NAME_Renderer):
    GPU_Name = GPU_NAME_Device1
else:
    GPU_Name = GPU_NAME_Renderer

#GPU_Name = max(GPU_NAME_Device1, GPU_NAME_Renderer, key=lambda x: len(x))

########################################################################
##
##                        Monitors detection
##
########################################################################
	# plan A
if Graphic_server_installed=="x11":
	Monitors_Detected=os.popen("cat /var/log/Xorg.0.log | grep -E -i -w connected | tail -10 |  cut -c 19- | sort | uniq | grep -oP '^[^\:]*\: \K[^\:]+' | sed 's/[(][^)]*[)]//g'").read().lstrip().rstrip().split('\n')

	# plan B
elif Graphic_server_installed=="wayland":
	Monitors_Detected=Inxi_Search("model: ",Total_Clean)

	# plan C
else:
	Monitors_Detected=os.popen("sh detect_screen.sh").read().rstrip().split('\n')


########################################################################
##
##                   Resolutions detection
##
########################################################################
Resolutions_Detected=Inxi_Search(" res:",Total_Clean)


########################################################################
##
##                 Connections detection
##
########################################################################
Connections_Detected=Inxi_Search("Monitor",Total_Clean)







# ########################################################################
# ##
# ##                   DEBUG
# ##
# ########################################################################
# Ecrans=1
# if Ecrans==1:
# 	Monitors_Detected = ['DELL P2412H ']
# 	Resolutions_Detected = ['1920x1080']
# 	Connections_Detected = ['1: DVI-I-1']

# if Ecrans==2:
# 	Monitors_Detected = ['DELL P2412H ', 'WOR TERRA 2225W']
# 	Resolutions_Detected = ['1920x1080', '1920x1080']
# 	Connections_Detected = ['1: DVI-I-1', '2: HDMI-0']


# if Ecrans==3:
# 	Monitors_Detected = ['DELL P2412H ', 'WOR TERRA 2225W', 'WOR TERRA 2225W']
# 	Resolutions_Detected = ['1920x1080', '1920x1080', '1920x1080']
# 	Connections_Detected = ['1: DVI-I-1', '2: HDMI-0', '3: HDMI-0']


# if Ecrans==4:
# 	Monitors_Detected = ['DELL P2412H ', 'WOR TERRA 2225W','DELL P2412H ', 'WOR TERRA 2225W']
# 	Resolutions_Detected = ['1920x1080', '1920x1080', '1920x1080', '1920x1080']
# 	Connections_Detected = ['1: DVI-I-1', '2: HDMI-0', '3: HDMI-0','4: DVI-I-1',]



########################################################################
##
##                      GPUS detection
##
########################################################################
GPU_maker=os.popen("lspci | grep -i 'vga\|3d\|2d'").read().rstrip().split('\n')[0]
	


########################################################################
##
##      Conky syntax for monitors, resolutions and connections
##
########################################################################


Monitors_Total_Text=""
for count,value in enumerate(Monitors_Detected):
    phrase="""${offset 0}${color gold}"""+Monitor[Language]+""" """+str(count+1)+"""${color}: """+Monitors_Detected[count]+"""${alignc -120}"""+Resolutions_Detected[count]+"""${alignr 0}"""+Connections_Detected[count]+"\n"
    #Monitors_Total_Text=Phrase_Total+phrase
    Monitors_Total_Text=Monitors_Total_Text+phrase

txt01="""
gap_x = 1020,
gap_y = 50,
minimum_width = 400, 
maximum_width = 400,
minimum_height = 50,

lua_load = 'allcombined.lua',
};

conky.text = [[
${image icons/graphic_card.png -p 0,0 -s 30x30}
${offset 35}${font Good Times:size=12}${color Tan1}"""+Display[Language]+"""${color}${hr 2}${font}
${color gold}${font Ubuntu-Title:size=10}"""+Display_server[Language] + """ : ${color}"""+Graphic_server_installed+""" ${font Ubuntu-Title:size=10}
"""+Monitors_Total_Text


Total_Conky_Text=""

#Height_conky=70+2*32

Height_conky=102+len(Connections_Detected)*16

if "nvidia" in GPU_maker.lower():
	Total_Conky_Text = Middle_text(Height_conky)
	GPU_Line=""

else:

	GPU_Line="${offset 0}${color gold}GPU : ${color}"+GPU_Name


total=header+txt01+"\n"+GPU_Line+Total_Conky_Text + "\n]];"
Write_File('displayfile',total) 
