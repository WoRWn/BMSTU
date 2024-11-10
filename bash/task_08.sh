#!/bin/bash

read -r A
if [[ "$A" =~ ^[1-9][0-9]*$ ]]; then
    result=$((A * A))
    echo $result
else
    echo "$A$A"
fi