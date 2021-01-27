#!/bin/bash

# kali

pkg=$(apt-get -q -y --ignore-hold --allow-change-held-packages --allow-unauthenticated -s dist-upgrade | /bin/grep  ^Inst | wc -l)

if [[ "$pkg" != "0" ]]
then
	white='%{F#ffffff}'
	echo "${white}$pkg "
fi
