"""
Author: Greg Lee
Date: 2/21/18
Class: Scripting for Cyber Security
Purpose: This program extracts the image name, size, camera used to take the photo, GPS info and date that the photo was taken. Then the MD5 hash is generated, then compared to a list of MD5 hashs from the FBI. If the hashes match then the image is flagged as illicit and the image's info is outputted to the screen.
"""

import exifread
import os
import hashlib

# Image class is used to help organize the data from the image
class Image:
    #initilizer
    def __init__(self, name, image_make, image_model, image_gpsInfo, image_date, dimension_width, dimension_height, md5hash, illicit):
        self.name = name
        self.image_make = image_make
        self.image_model = image_model
        self.image_gpsInfo = image_gpsInfo
        self.image_date = image_date
        self.dimension_width = dimension_width
        self.dimension_height = dimension_height
        self.md5hash = md5hash
        self.illicit = illicit

# this function returns the MD5 hash of a file
def getMD5Hash(name):
    md5 = hashlib.md5()
    with open(name, 'rb') as file:
        temp = file.read()
        md5.update(temp)
    return md5.hexdigest()

#this function returns the data found in the exif property
def getPhotoData(data, property):
    if property in data:
        return data[property]

def main():
    #init variables to store image properties
    name = ""
    image_make = ""
    image_model = ""
    image_date = ""
    image_gpsInfo = ""
    dimension_width = ""
    dimension_height = ""
    md5hash = ""
    illicit = ""

    imageList = [] #init list to hold the images
    imageDataList = [] #init list to hold the Image objects

    #searches the current working directory for jpegs/jpg files and adds them to the imageList
    for file in os.listdir(os.getcwd()):
      if 'jpg' in file or 'jpeg' in file or 'JPG' in file or 'JPEG' in file:
          imageList.append(file)

    #load hash values from FBI list into a list and then remove the \n from each line
    hashList = []
    f = open('FBI Image Hash.txt', 'r')
    hashList = f.readlines()
    hashList = [hash.rstrip('\n') for hash in hashList]

    #gets the properties from each image and generates the MD5hash for each image. The generated hash is then compared to the list from the FBI, if it matches then illicit is set to Yes. Then the data is put into an Image object and appended to a list
    for file in imageList:
        f = open(file, 'rb')
        data = exifread.process_file(f, details=False)
        image_make = getPhotoData(data, 'Image Make')
        image_model = getPhotoData(data, 'Image Model')
        image_date = getPhotoData(data, 'Image DateTime')
        dimension_width = getPhotoData(data, 'EXIF ExifImageWidth')
        dimension_height = getPhotoData(data, 'EXIF ExifImageLength')
        md5hash = getMD5Hash(file)

        if md5hash in hashList:
            illicit = 'Yes'
        else:
            illicit = 'No'

        temp = Image(file, image_make, image_model, image_gpsInfo, image_date, dimension_width, dimension_height, md5hash, illicit)
        imageDataList.append(temp)

    #print out data for the illegal image
    print("Most likely to be an illicit image")
    print("====================================")
    for img in imageDataList:
        if img.illicit == 'Yes':
            print("Illicit: {}".format(img.illicit))
            print("Filename: {}".format(img.name))
            print("Image Dimensions (WxH): {} x {}".format(img.dimension_width, img.dimension_height))
            print("Camera: {} {}".format(img.image_make, img.image_model))
            print("GPS Coordinates:  {}".format(img.image_gpsInfo))
            print("Date taken: {}".format(img.image_date))
            print("MD5 hash: {}".format(img.md5hash))
            print("====================================")


if __name__ == "__main__":
    main()
