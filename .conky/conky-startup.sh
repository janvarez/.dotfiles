#!/bin/sh

if [ "$DESKTOP_SESSION" = "ubuntu" ]; then 
   sleep 20s
   killall conky
   cd "$HOME/.conky/AutomatiK"
   conky -c "$HOME/.conky/AutomatiK/cpufile" &
   cd "$HOME/.conky/AutomatiK"
   conky -c "$HOME/.conky/AutomatiK/diskfile" &
   cd "$HOME/.conky/AutomatiK"
   conky -c "$HOME/.conky/AutomatiK/displayfile" &
   cd "$HOME/.conky/AutomatiK"
   conky -c "$HOME/.conky/AutomatiK/infofile" &
   cd "$HOME/.conky/AutomatiK"
   conky -c "$HOME/.conky/AutomatiK/memfile" &
   cd "$HOME/.conky/AutomatiK"
   conky -c "$HOME/.conky/AutomatiK/netfile" &
   exit 0
fi
