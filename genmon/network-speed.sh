#!/bin/sh

# An example script for the genmon plugin displaying the bandwidth.
# pass the interface name as first parameter to the script
# cat /sys/class/net/ to see all available interfaces

interface=$1

# added so as to recover from a corrupt run
# where the netlog file is written in 
# improper format
if [[ $(wc /tmp/netlog | awk '{print $2}') < 3 ]] ; then
	rm /tmp/netlog
fi

#wlp0s20f3 - wifi
test -d /sys/class/net/$interface

# Handle unknown interface
if [ $? -ne "0" ]; then
	echo "No statistics for $interface"
	exit
fi
now=$(date +"%s%N")
crx=$(cat "/sys/class/net/$interface/statistics/rx_bytes")
ctx=$(cat "/sys/class/net/$interface/statistics/tx_bytes")

# Handle condition when the script is run for first time
test -f /tmp/netlog
if [ $? -ne "0" ]; then
	printf "$now $crx $ctx" > /tmp/netlog
	echo First Run
	exit
fi

netlog=$(cat /tmp/netlog)
olddata=($netlog)

dt=$(($now - ${olddata[0]}))
drx=$(($crx - ${olddata[1]}))
dtx=$(($ctx - ${olddata[2]}))

rx=$(( ($drx * 1000000000) / ($dt * 1024) ))
tx=$(( ($dtx * 1000000000) / ($dt * 1024) ))

printf "$now $crx $ctx" > /tmp/netlog

printf "<txt><span color='#ee77aa'>% 5d ↑</span>\n<span color='#77aaee'>% 5d ↓</span></txt>\n" $tx $rx 
printf "<tool>Bandwidth on interface <b>$interface</b></tool>" 
