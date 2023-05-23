#!/bin/bash

# bash script to change network interface into monitor mode (and back to managed mode)

# check sudo & display help menu
if [ -z "$1" ] || [[ $1 == *"-h"* ]]
then
    echo '''[usage]:  `./monitor-mode <interface> <mode>`

interface -> network interface to change
mode      -> `mon` for monitor mode
             `man` for managed mode

RUN script as ROOT: `sudo ./monitor-mode <interface> <mode>`'''
exit
fi


echo [#] initiating change protocol

# taking interface down
ip link set $1 down > /dev/null 2>&1

# checking interface before changing
check1=$(iw $1 info | grep type)


# changing to monitor / managed mode
if [[ $2 == "man" ]]
then
	iw $1 set type managed > /dev/null 2>&1
	echo '[#] '$1' -> MANAGED MODE: activated'
elif [[ $2 == "mon" ]]
then
	iw $1 set monitor control > /dev/null 2>&1
	echo '[#] '$1' -> MONITOR MODE: activated'
else
	echo '''[!] <mode> -> only `mon`/`man` accepted 
    (run `./monitor-mode` to display help menu)'''
    ip link set $1 up > /dev/null 2>&1
    exit
fi


# taking interface up
ip link set $1 up > /dev/null 2>&1

# checking interface after changing
check2=$(iw $1 info | grep type)

if [[ $check1 == *man* ]] && [[ $check2 == *mon* ]] || [[ $check1 == *mon* ]] && [[ $check2 == *man* ]]
then
	echo [#] mode successfully changed
else
	echo '''[!] mode change unsuccessful
    (RUN script as ROOT: `sudo ./monitor-mode <interface> <mode>`)'''
fi
