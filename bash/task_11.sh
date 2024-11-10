#!/bin/bash

read -r A
if [[ $A -ge 0 ]]; then
    for ((i = 0; i <= A/2; i++)); do
        echo "$i"
    done
fi
