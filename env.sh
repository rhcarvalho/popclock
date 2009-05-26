#!/bin/bash

#hack to load profile crontab
. ~/.profile
export DISPLAY=:0.0
POPCLOCKHOME=$HOME/Projetos/PopClock

$POPCLOCKHOME/PopClock $*
