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

mkdir -p $directory;
baseurl=$(echo $url | grep -oE "https?://[a-z.\-]+")

echo Downloading $url
curl -s $url | grep -oE "<img[^>]*src=[^>]*>" | \
  sed 's/<img[^>]*src=\"\{0,1\}\([^> "]*\).*/\1/g' | \
  sed "s|^//||" > /tmp/$$.download.list.bak 

mkdir $directory/download/
cd $directory/download/

while read filename
do
  echo Downloading $filename
  curl -s -O "$filename"
done < /tmp/$$.download.list.bak

rm /tmp/$$.download.list.bak

