# -*- encoding: utf-8 -*-
import os
import platform
from useful_modules import *
from translations import *
Language=detect_language()

header = open('header.py', 'r').read()



#global Language

Session_WM=os.popen('echo $XDG_CURRENT_DESKTOP').read()
if Session_WM == "":
	Session_WM=os.popen('echo $DESKTOP_SESSION').read()


# determine installed language
Language_installed=os.popen("locale | grep LANG").read()
# print Language_installed




#PresenceOfBattery=os.popen("grep POWER_SUPPLY_CAPACITY /sys/class/power_supply/BAT1/uevent").read().split()
# print PresenceOfBattery
# if PresenceOfBattery==[]:
# 	print "pas de batterie"



# print Arch
# | tr '[:upper:]' '[:lower:]'
#DistroID=os.popen("lsb_release -si | tr '[:upper:]' '[:lower:]'").read()

# to get all the needed information
#os.system("source /etc/os-release")

#DistroID=os.popen("lsb_release -a || cat /etc/redhat-release || cat /etc/*-release || cat /etc/issue").read().lower()
DistroID=os.popen("lsb_release -ds 2>/dev/null || cat /etc/*release 2>/dev/null | head -n1 || uname -om").read().lower()

DistroID = DistroID.strip('\n')


if 'ubuntu' in DistroID:
	#Session_WM=os.popen('echo $XDG_CURRENT_DESKTOP').read()

	if "kde" in Session_WM:
			LOGO="logo-kubuntu.png"
	elif "xfce" in Session_WM:
			LOGO="logo-xubuntu.png"
	else:
			LOGO="logo-ubuntu.png"

elif 'pclinux' in DistroID:
		LOGO="logo-PC-LinuxOS.png"

elif 'mandr' in DistroID:
		if 'pclinux' in platform.dist()[2].lower():
			LOGO="logo-PC-LinuxOS.png"
		else:
			LOGO="logo-mandriva.png"

elif 'pepper' in DistroID:
		LOGO="logo-peppermint.png"

elif 'endeavour' in DistroID:
		LOGO="logo-endeavour.png"



elif 'antix' in DistroID:
		LOGO="logo-antix.png"


elif 'mint' in DistroID:
		LOGO="logo-mint.png"

elif 'makululinux' in DistroID:
		LOGO="logo-makululinux.png"

elif 'suse' in DistroID:
		LOGO="logo-suse.png"

elif 'deepin' in DistroID:
		LOGO="logo-deepin.png"

elif 'debian' in DistroID:
		LOGO="logo-debian.png"

elif 'fedora' in DistroID:
		LOGO="logo-fedora.png"

elif 'mepis' in DistroID:
		LOGO="logo-mepis.png"

elif 'pop' in DistroID:
		LOGO="logo-popos.png"


elif 'sabayon' in DistroID:
		LOGO="logo-sabayon.png"

elif 'centos' in DistroID:
		LOGO="logo-centos.png"

elif 'puppy' in DistroID:
		LOGO="logo-puppy.png"

elif 'elementary' in DistroID:
		LOGO="logo-elementary.png"

elif 'mageia' in DistroID:
		LOGO="logo-mageia.png"

elif 'gentoo' in DistroID:
		LOGO="logo-gentoo.png"

elif 'hat' in DistroID:
		LOGO="logo-red-hat.png"

elif 'slackware' in DistroID:
		LOGO="logo-slackware.png"

elif 'arch' in DistroID:
		LOGO="logo-arch.png"

elif 'mx' in DistroID:
		LOGO="logo-mx.png"


elif 'zorin' in DistroID:
		LOGO="logo-zorin.png"

elif 'linspire' in DistroID:
		LOGO="logo-linspire.png"

elif 'lxle' in DistroID:
		LOGO="logo-lxle.png"

elif 'manjaro' in DistroID:
		LOGO="logo-manjaro.png"

elif 'raspbian' in DistroID:
		LOGO="logo-raspbian.png"

elif 'antergos' in DistroID:
		LOGO="logo-antergos.png"

elif 'lite' in DistroID:
		LOGO="logo-lite.png"

elif 'garuda' in DistroID:
		LOGO="logo-garuda.png"

elif 'parrot' in DistroID:
		LOGO="logo-parrot.png"


elif 'linuxfx' in DistroID:
		LOGO="logo-linuxfx.png"


else:
		LOGO="logo-tux.png"

#LOGO="logo-parrot.png"

PathToLOGO="${image logo/"+LOGO+" -p 5,40 -s 64x64}"




#grep POWER_SUPPLY_CAPACITY /sys/class/power_supply/BAT1/uevent


UserHost=os.popen("echo `whoami`@`hostname`").read()
UserHost=User2[Language]+""":${alignr}"""+UserHost


# print UserHost



# print SystemInformation[Language]






txt01="""	
	gap_x = 15,
	gap_y = 50,
};
conky.text = [[
${image icons/information.png -p 0,0 -s 30x30}
${offset 35}${font Good Times:size=12}${color Tan1}"""+SystemInformation[Language]+""" ${color}${hr 2}${font}
""" 
txt02="""${goto 80}${color red}${font Ubuntu-Title:size=11}"""+DistroID+"""${font}${color} | """
txt03="""${goto 80}"""+Kernel[Language]+"""${alignr} $kernel $machine
${goto 80}"""+Uptime[Language]+"""${alignr}$uptime
#${font DJB Get Digital:size=30}${tab 90}${time %H:%M:%S}
]];
"""



total=header+txt01+txt02+Session_WM+"${goto 80}"+UserHost+PathToLOGO+txt03
# print total


Write_File('infofile',total)
