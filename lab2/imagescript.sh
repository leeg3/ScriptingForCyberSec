#***********************************
# Author: Greg Lee
# Date: 1/16/17
# Description: Search all images/directory for images and return the owner, full path of image, and hash
# Note: Files were placed in a sub directory from where this script is stored 
#***********************************

#!/bin/bash
declare -a IMAGELIST
declare -a TYPELIST
declare -a OWNERLIST
declare -a PATHLIST
declare -a MD5LIST
declare -a SHA1LIST

#get number of images in this dir and subdir
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' > TEMP
result=( $(wc < TEMP) ) # 20 in my environment 
echo $result

NUM=0 
#get all image files
echo "All images in this directory and subdirectory" > results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' | cut -d ':' -f1 | while read line; do basename $line; done | while read line; do if [ "$NUM" -le "$result" ]; then echo $line; fi; NUM=$((NUM + 1)); done 
# IMAGELIST[$NUM]=$line; NUM=$((NUM + 1)); done  >> results.txt
echo "========================================================" >> results.txt

#echo ${IMAGELIST[10]} >> results.txt

#get all image file types
echo "All image types in this directory and subdirectory" >> results.txt 
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' | cut -d ':' -f2 >> results.txt
echo "========================================================" >> results.txt


#get all owners of each file 
echo "Owners of each image that is in this directory and subdirectory" >> results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' | cut -d ':' -f1 | while read -r line; do stat -f %Su $line; done >> results.txt 
echo "========================================================" >> results.txt


#get the full path of the file 
echo "Full path of each image in this directory and subdirectory" >> results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' | cut -d ':' -f1 | while read line; do basename $line; done | while read line; do find $PWD -name $line; done >> results.txt
echo "========================================================" >> results.txt


#get md5 hash of each file 
echo "MD5 hash of each image in this directory and subdirectory" >> results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' | cut -d ':' -f1 | while read line; do md5 $line; done | cut -d \= -f2 >> results.txt
echo "========================================================" >> results.txt


#get SHA1 hash of each file
echo "SHA1 hash of each image in this directory and subdirectory" >> results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' | cut -d ':' -f1 | while read line; do shasum $line; done | cut -d \. -f 1 >> results.txt
echo "========================================================" >> results.txt

#TMP=10
#IMAGELIST[$TMP]=TOTTO.PNG

TEMP=0
while [[ "$TEMP" -le 20 ]]; do 
	echo ${IMAGELIST[$TEMP]}
	TEMP=$((TEMP + 1))
done

cat results.txt
#clean up 
