#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 filename"; exit
elif [ -e "$1" ] && [ -f "$1" ]; then
  filename=$1; echo "File: $filename"
else
  echo "Invalid file name"
fi  

grep -oE "\b[a-zA-Z]+\b" "$filename" | \
  awk ' { count[$0]++ }
    END { printf("%-14s %s\n", "Word", "Count") ;
      for ( i in count )
        { printf("%-14s %s\n", i, count[i]); } } '
