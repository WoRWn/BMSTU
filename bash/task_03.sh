#!/bin/bash

if [[ -z "$VAR1" ]]; then
    echo "ERROR"
else
    if [[ "$VAR1" =~ ^-?[0-9]+$ ]]; then
        result=$((VAR1 * VAR1))
        echo "$result"
    else
        result="${VAR1}mama${VAR1}"
        echo "$result"
    fi
fi