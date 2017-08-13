#!/bin/bash

cd /home/pi/src/eagle
logger -p local6.warn "Pull updates for phoenix-eagle"
/usr/bin/git pull

cd /home/pi/src/eagleweb
logger -p local6.warn "Pull updates for phoenix-eagleweb"
/usr/bin/git pull

