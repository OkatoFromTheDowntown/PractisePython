#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Usage: $0 URL -d Directory"; exit
fi

while [ $# -gt 0 ] 
do
  case $1 in
    -d)   shift; directory=$1; shift ;;
    *)    url=$1; shift ;;
  esac
done

mkdir -p "$directory"/download;
baseurl=$(echo "$url" | grep -oE "https?://[a-z.\-]+")

echo Downloading "$url"
curl -s "$url" | grep -oE "<img[^>]*src=[^>]*>" | \
  sed 's/<img[^>]*src=\"\{0,1\}\([^> "]*\).*/\1/g' | \
  sed -e "s|^//||" -e "s|^/|$baseurl|" > "$directory"/download/$$.download.list.bak 

cd "$directory"/download/

while read filename
do
  echo Downloading "$filename"
  curl -s -O "$filename"
done < ./$$.download.list.bak

