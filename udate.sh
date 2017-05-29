#!/bin/bash

read IDm
read condition

target="`cat database.txt|grep $IDm|awk '{print $1 " " $2}'`"

sed "/$IDm/d" -i database.txt

echo "$target $condition" >> database.txt

sed '/^\s/d' -i database.txt

