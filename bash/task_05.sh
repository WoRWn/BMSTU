#!/bin/bash

read -r A
read -r B
sum=$((A + B))
sum_2=$((A + B * B))
diff=$((A * A - B * B))
echo "$sum $sum_2 $diff"

