#!/bin/bash

if [[ -z "$VAR1" || -z "$VAR2" || -z "$VAR3" ]]; then
    echo "ERROR"
else
    if [[ "${VAR1,,}" == "yes" ]]; then
        result=$((VAR2+VAR3))
        echo $result
    else
        result=$((VAR2+VAR2+VAR3))
        echo $result
    fi
fi