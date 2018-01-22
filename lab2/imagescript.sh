#***********************************
# Author: Greg Lee
# Date: 1/16/17
# Description: Search all images/directory for images and return the owner, full path of image, and hash
# Note: Files were placed in a sub directory from where this script is stored 
#***********************************


#!/bin/bash
#declare -a RESULT
#IMAGELIST=
OWNERLIST=
PATHLIST=
RESULTS=

#find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' > TEMP
#result=( $(wc < TEMP) )
#NUM=${result[0]}
 
#get all image files
echo "All images in this directory and subdirectory" > results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' >> results.txt
echo "=======================================================" >> results.txt

#get all owners of each file 
echo "Owners of each image that is in this directory and subdirectory" >> results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' | cut -d ':' -f1 | while read -r line; do stat -f %Su $line; done >> results.txt 
echo "=======================================================" >> results.txt

#get the full path of the file 
echo "Full path of each image in this directory and subdirectory" >> results.txt
find . -type f -exec file {} \; | grep -i -o -E '^.+: \w+ image' |  while read -r line; do pwd $line; done >> results.txt
echo "=======================================================" >> results.txt


cat results.txt
#put results into a file?
#zero=0
#while [ "$zero" -le "$NUM" ]
#do
#	echo ${IMAGELIST[$zero]}
# 	let NUM=NUM-1
#done  

#clean up 
