#!/bin/bash

if [ $# -eq 0 ]; then
  path='.'
elif [ $# -ne 1 ]; then
  echo "usage: $0 basepath"
elif [ ! -e "$1" ]; then
  echo "invalid basepath: $1"
else
  path=$1
fi

declare -A opStorage;

while read line;
do
  ftype=`file -b "$line" | cut -d, -f1`;
  ((opStorage["$ftype"]++))
done < <(find "$path" -type f -print)

echo ============= File types and counts ============= 
for ftype in "${!opStorage[@]}";
do
  echo $ftype : ${opStorage["$ftype"]}
done

