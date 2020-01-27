#!/bin/bash

for ip in $(seq 1 254); do
	ping -c 1 10.10.10.$ip | grep "bytes from" | cut -d " " -f4 | cut -d ":" -f 1 &
done
