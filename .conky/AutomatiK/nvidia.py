# -*- encoding: utf-8 -*-
import os
from translations import *
from useful_modules import *

Language=detect_language()


def Middle_text(Height_conky):
	#Height_conky=84


	########################################################################
	##
	##                        Minimum and Maximum Frequencies
	##
	########################################################################

	Maximum_Frequency = os.popen("nvidia-smi -q -d SUPPORTED_CLOCKS | grep Memory | grep -Eo '[0-9]{1,4}' | head -1").read().rstrip().split('\n')[0]
	Minimum_Frequency = os.popen("nvidia-smi -q -d SUPPORTED_CLOCKS | grep Graphics | grep -Eo '[0-9]{1,4}' | tail -1").read().rstrip().split('\n')[0]


	########################################################################
	##
	##                      Maximum temperature
	##
	########################################################################

	Maximum_Temperature = os.popen("nvidia-smi -q -d SUPPORTED_GPU_TARGET_TEMP | grep Max | grep -Eo '[0-9]{1,4}' | tail -1").read().rstrip().split('\n')[0]
	if Maximum_Temperature=='':
		Maximum_Temperature='85'


	########################################################################
	##
	##                        Total Memory
	##
	########################################################################

	Total_Memory = os.popen("nvidia-smi --query-gpu=memory.total --format=csv | tail -1 |  grep -Eo '[0-9]{1,4}'").read().rstrip().split('\n')[0]


	########################################################################
	##
	##                        Driver version
	##
	########################################################################

	Driver_Version=os.popen("nvidia-smi --query-gpu=driver_version --format=csv | grep -vwE '(driver_version)'").read().rstrip().split('\n')[0]


	########################################################################
	##
	##                        Gpu_Name
	##
	########################################################################

	Gpu_Name=os.popen("nvidia-smi --query-gpu=gpu_name --format=csv | grep -vwE '(name)'").read().rstrip().split('\n')[0] # find the cards


	########################################################################
	##
	##                        Set Logo
	##
	########################################################################

	LOGO="Nvidia_logo.png"
	PathToLOGO="${image img/"+LOGO+" -p 327,"+str(int(Height_conky+7))+"}"


	########################################################################
	##
	##                        Set Frequency text and bar
	##
	########################################################################

	Frequency_Text=Frequency[Language]+"${alignr 80}${nvidia memfreq} / "+str(Maximum_Frequency)+" Mhz"
	#Frequency_Bar='${lua gradbar {6,'+str(Height_conky)+', "${nvidia memfreq}" ,'+str(Maximum_Frequency)+', 105, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}	${image img/trans-bg240.png -p 3,'+str(Height_conky-5)+' -s 314x11}'
	Frequency_Bar_List=[]
	F1='${lua gradbar {6,'
	F2 =str(Height_conky) 
	F3=', "${nvidia memfreq}" ,'
	F4=str(Maximum_Frequency)
	F5=', 105, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}	${image img/trans-bg240.png -p 3,'
	F6=str(Height_conky-5)
	F7=' -s 314x11}'
	Frequency_Bar_List.append(F1)
	Frequency_Bar_List.append(F2)	
	Frequency_Bar_List.append(F3)
	Frequency_Bar_List.append(F4)		
	Frequency_Bar_List.append(F5)
	Frequency_Bar_List.append(F6)
	Frequency_Bar_List.append(F7)
	Frequency_Bar=''.join(Frequency_Bar_List)



	########################################################################
	##
	##                        Set Memory text and bar
	##
	########################################################################

	Card=0
	Memory_Text=Ram[Language]+"${alignr 80}${exec nvidia-settings -q [gpu:"+str(Card)+"]/UsedDedicatedGPUMemory -t} / ${exec nvidia-settings -q [gpu:"+str(Card)+"]/TotalDedicatedGPUMemory -t} MiB "
	Memory_Bar_List=[]
	M1="${lua gradbar {6, "+str(Height_conky+32)+" ,"
	M2='"${exec nvidia-settings -q [gpu:'
	M3=str(Card)
	M4=']/UsedDedicatedGPUMemory -t}"'
	M5=","+Total_Memory+" , 105, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}${image img/trans-bg240.png -p 3,"
	M6=str(Height_conky+28)
	M7=' -s 314x11}'
	Memory_Bar_List.append(M1)
	Memory_Bar_List.append(M2)	
	Memory_Bar_List.append(M3)
	Memory_Bar_List.append(M4)
	Memory_Bar_List.append(M5)
	Memory_Bar_List.append(M6)
	Memory_Bar_List.append(M7)		
	Memory_Bar=''.join(Memory_Bar_List)



	########################################################################
	##
	##                        Set Temperature text and bar
	##
	########################################################################

	Temperature_Text=Temperature[Language]+" ${alignr 80} ${exec nvidia-settings -q [thermalsensor:"+str(Card)+"]/ThermalSensorReading -t} °C"
	Temperature_Bar_List=[]
	T1="${lua gradbar {6, "+str(Height_conky+64)+" ,"
	T2='"${exec nvidia-settings -q [thermalsensor:'
	T3=str(Card)
	T4=']/ThermalSensorReading -t}" ,'+Maximum_Temperature+', 105, 2, 10, 1, 0xFFFFFF, 0.25, 0x00FF00, 1, 0xFFFF00, 1, 0xFF0000, 1}}${image img/trans-bg240.png -p 3,'
	T5=str(Height_conky+60)
	T6=" -s 314x11}"
	Temperature_Bar_List.append(T1)
	Temperature_Bar_List.append(T2)
	Temperature_Bar_List.append(T3)	
	Temperature_Bar_List.append(T4)
	Temperature_Bar_List.append(T5)
	Temperature_Bar_List.append(T6)	
	Temperature_Bar=''.join(Temperature_Bar_List)			



		# 		# detect Maximum clock speed
		# 		MaximumClock=os.popen("nvidia-settings -q all -t  | grep GPUCurrentClockFreqs:").read().split(",")
		# 		MaximumClock=(MaximumClock[len(MaximumClock)-1:])
		# 		MaximumClock=MaximumClock[0].rstrip()
		# 		#print (MaximumClock)
		# 		# detect Screen Resolution
		# 		ScreenResolution=os.popen("nvidia-settings -q ScreenPosition -t").read()
		# 		ScreenResolution = ScreenResolution.replace(' ','').split(',')
		# 		Width=ScreenResolution[2].split('=')[1].rstrip()
		# 		Height=ScreenResolution[3].split('=')[1].rstrip()
		# 		RefreshRate=os.popen("nvidia-settings -q [dpy:1]/RefreshRate -t").read().rstrip()
		# 		DriverVersion=os.popen("nvidia-settings -q 0/NvidiaDriverVersion -t").read().rstrip()
		# 		#print (Width)
		# 		#print (Height)
		# 		TotalMemory=os.popen("nvidia-settings -q [gpu:0]/TotalDedicatedGPUMemory -t").read()
		# 		#print TotalMemory
		# 		Num=Num+1
		# else:
		# 			CardName=CardName+" - No nvidia drivers found !          "
		# 			ConnectorToDisplay=""
		# 			Width=os.popen("xrandr | grep '*' | awk '{ print $1}'").read().rstrip()
		# 			Height=""
		# 			RefreshRate=""
		# 			DriverVersion=""
		# 			MaximumClock=""
		# 			TotalMemory=""


	txtNvidia=PathToLOGO+"${offset 0}${color gold}GPU : ${color}"+Gpu_Name+"\n"+Frequency_Text+"\n"+Frequency_Bar+"\n"+Memory_Text+"\n"+Memory_Bar+"\n"+Temperature_Text+"\n"+Temperature_Bar+"\n${color gold}Driver : ${color}"+Driver_Version
	return txtNvidia
