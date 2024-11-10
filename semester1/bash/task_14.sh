#!/bin/bash

sum=0
for num in "$@"; do
    if [[ "$num" =~ ^-?[0-9]+$ ]]; then
        sum=$((sum+num))
    fi
done
echo "$sum"