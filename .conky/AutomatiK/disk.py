# -*- encoding: utf-8 -*-
import os,time
header = open('header.py', 'r').read()
from useful_modules import *
from translations import *
Language=detect_language()



DF_ROOT="df -Th 2>/dev/null | grep -E 'dev|media' | grep -E -v '^.*(tmp|proc|sys|var|pts|daemon|root|gvfs|efi|snap|.Private).*$'"


List_Of_Devices=[]
#time.sleep(5)
#  /dev/sda1
Command=DF_ROOT+"| awk '{ print $1}'"
Partition_Name=os.popen(Command).read().split() 





# ext4
Command=DF_ROOT+"| awk '{ print $2}'"
File_Type=os.popen(Command).read().split()


# Size
Command=DF_ROOT+"| awk '{ print $3}'"
Partition_Size=os.popen(Command).read().split()


#  /media/data_zalman
Command=DF_ROOT+"| awk '{ print $7}'"
Mount_Point=os.popen(Command).read().split()
#print Mount_Point, len(Mount_Point)

	


#  print Mount_Point

#for dev in List_Of_Mounted_Partitions:
#	dev=dev.replace('\\040'," ")
#	List_Of_Mounted_Partitions[i]=dev
#	i=i+1




txt01="""
gap_x = 685,
	gap_y = 50,

	lua_load = 'allcombined.lua',

};

conky.text = [[
${image icons/hard_drive.png -p 0,0 -s 30x30}
${offset 35}${font Good Times:size=12}${color Tan1}"""+DiskUsage[Language]+""" ${color}${hr 2}${font}
"""

#${lua gradbar 100 140 ${cpu 3} 100 40 2 10 1 0xFFFFFF 0.25 0x00FF00 1 0xFFFF00 1 0xFF0000 1}
#Graph="${color #FFEF00}${offset 5}${fs_bar 8,200 "+Mount_Point[num]+"}"
List = []
Height=70
for num in range(len(Partition_Name)):
	if len (Mount_Point[num])>35:
		Truncated=Mount_Point[num][0:35]+"~"
		Mount=" ${color}"+Truncated+"\n"
	else:
		Mount=" ${color}"+Mount_Point[num]+"\n"
	Graph='${lua gradbar {6, '+str(Height)+', "${fs_used_perc '+Mount_Point[num]+'}" ,100, 75, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}'
	PercentUsed="${alignr}${offset -5}${fs_used_perc "+Mount_Point[num]+"}% "+UsedWord[Language]+"\n"
	if len (Partition_Name[num])>18:
		Truncated=Partition_Name[num][0:18]+"~"		
		DriveName=" "+Truncated+" = "+Partition_Size[num]+" (${fs_type "+Mount_Point[num]+"})"
	else:		
		DriveName=" "+Partition_Name[num]+" = "+Partition_Size[num]+" (${fs_type "+Mount_Point[num]+"})"
	FreeSpace="${color}${alignr}${offset -5}${fs_free "+Mount_Point[num]+"} "+FreeWord[Language]+"\n"
	Separator="${color}${hr 1}"+"\n\n"
	BackgroundImage="${image img/trans-bg240.png -p 4,"+str(Height-5)+" -s 226x11}"

	List.append(Mount)
	List.append(Graph)
	List.append(PercentUsed)
	List.append(DriveName)
	List.append(FreeSpace)
	List.append(Separator)
	List.append(BackgroundImage)
	Height=Height+75
TotalDisk=''.join(List)
#print ("TotalDisk",TotalDisk)

#${lua gradbar {6, 70, "${fs_used_perc /}" ,100, 75, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}${alignr}${offset -5}${fs_used_perc /}% utilisés

txt02="""${color lightgrey}"""+DiskReading[Language]+""": $color${diskio_read}${alignr}${color lightgrey}"""+DiskWriting[Language]+""": ${color}${diskio_write}
${color #000000}${diskiograph_read 12,145 000000 EEEEEE}${alignr}${color #000000}${diskiograph_write 12,145 000000 EEEEEE}
"""




total=header+"\n"+txt01+"\n"+TotalDisk+"\n"+txt02 + "]];"
#print total

Write_File('diskfile',total)
