#!/bin/bash

read -r A
result=""
if [[ $A -ge 0 ]]; then
    for ((i = 0; i <= A/3; i++)); do
        result+="$i "
    done
fi
echo -n "$result"
