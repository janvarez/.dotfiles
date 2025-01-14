#!/bin/bash
#xdpyinfo | grep dots
xrandr --dpi 96
cd $(dirname $0)
killall conky
rm infofile
rm clockfile
rm memfile
rm cpufile
rm topfile
rm diskfile
rm netfile
rm displayfile

python3 kill_started_polls_processes.py
mkdir ~/.fonts > /dev/null 2>&1 
cp fonts/*.*tf ~/.fonts > /dev/null 2>&1 

mkdir ~/.local/share/fonts/ > /dev/null 2>&1 
cp fonts/*.*tf ~/.local/share/fonts/ > /dev/null 2>&1 
fc-cache ~/.fonts

python3 info.py 
python3 clock.py
python3 mem.py
python3 cpu.py
python3 top.py
python3 disk.py
python3 net.py
python3 display.py

conky -q -c infofile
conky -q -c clockfile
conky -q -c memfile
conky -q -c cpufile
conky -q -c topfile
conky -q -c diskfile
conky -q -c netfile
conky -q -c rssnews
conky -q -c displayfile
python3 poll_disk.py &
python3 poll_day.py &
#notify-send -i ~/AutomatiK/AutomatiK.png \
#"Information" \
#"Automatik is started\
#To move the widgets around the desktop,\
#use Alt+ left-Click"
