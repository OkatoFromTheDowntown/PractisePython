#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Usage: $0 URL -d Directory"; exit
fi

while [ $# -gt 0 ] 
do
  case $1 in
  -d)   shift; directory=$1; shift ;;
  *)    url=$1; shift ;;
done

mkdir -p $directory;
baseurl=$(echo $url | grep -oE "https?://[a-z.\-]+")

echo Dowloading $url
curl -s $url | grep -oE "<img[^>]*src=[^>]*>" | \
  sed 's/<img[^>]*src=\"\([^>]*\).*/\1/g | \
