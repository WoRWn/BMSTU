#!/bin/bash

read -r A
read -r B
if [[ $B -ge 0 ]]; then
    for ((i = 0; i < B; i++)); do
        echo "$A"
    done
fi