#!/bin/bash

IFS=$'\n'

old=$(ps -eo command)
time=${1-300}
end=$((SECONDS+$time))
while [ $SECONDS -lt $end ]; do
	new=$(ps -eo command)
	diff <(echo "$old") <(echo "$new") | grep [\<\>]
	sleep 1
	old=$new
done
