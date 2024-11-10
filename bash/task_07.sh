#!/bin/bash

read -r A
if (( A % 2 == 0 )); then
    echo "MAMA"
else
    echo "PAPA"
fi