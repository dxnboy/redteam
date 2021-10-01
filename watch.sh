#!/bin/bash

IFS=$'\n'

old=$(ls -lah $1)
ls -lah $1
time=1000
time=${2-20}
end=$((SECONDS+$time))
echo '=========================================================================='
while [ $SECONDS -lt $end ]; do
	new=$(ls -lah $1)
	diff <(echo "$old") <(echo "$new") | grep [\<\>] | grep -v '< d\|> d'
	sleep 1
	old=$new
done
