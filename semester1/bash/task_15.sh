#!/bin/bash

sum=0
for num in "$@"; do
    if ! [[ "$num" =~ ^[-+]?[0-9]+$ ]]; then
        echo "ERROR"
        exit 1
    fi
    sum=$((sum+num))
done
echo "$sum"