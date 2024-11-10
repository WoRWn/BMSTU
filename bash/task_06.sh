#!/bin/bash

if [[ -z "$VAR1" ]]; then
    read -r VAR1
    result=$((VAR1 * VAR1))
    echo $result
else
    result=$((VAR1 * VAR1))
    echo $result
fi
