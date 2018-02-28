"""
Author: Greg Lee
Date: 2/6/18
Description: This script takes a user input UNIX formatted time (epoch format) and outputs a human-readable time. The user can also specifify a time format of either 12hr or 24hr, and what time zone to convert the inputted time to. This script does not account for daylight savings
"""

import datetime
import argparse

# init parser for command line args
parser = argparse.ArgumentParser()

# optional command line arguments
parser.add_argument("-t", "--timeformat", help="Time format") #-f flag for format
parser.add_argument("-z", "--timezone", help="Timezone")  #-z for timezone

#required command line arguments
parser.add_argument("time", help="Time")

#gets the command line arguments and sets them into args
args = parser.parse_args()

__author__ = 'Raymond Hansen'
__date__ = '20180130'
__version__ = '0.5'

def main():
	"""The main function queries the user for a UNIX epoch timestamp and calls unix_convert to process the input.
	:return: Nothing."""

	#declare and init tuple and variables
	timezones = (
	[['CET', 'MET', 'WAT', 'WEST'], 1],
	[['CAT', 'EET', 'IST', 'SAST', 'USZ1'], 2],
	[['EAT', 'FET', 'IOT', 'MSK', 'SYOT', 'TRT'], 3],
	[['AZT', 'GET', 'MUT', 'RET', 'SAMT', 'SCT', 'VOLT'], 4],
	[['HMT', 'MAWT', 'MVT', 'ORAT', 'PKT', 'TFT', 'TJT', 'TMT', 'UZT', 'YEKT'], 5],
	[['BIOT', 'BST', 'BTT', 'KGT', 'OMST', 'VOST'], 6],
	[['CXT', 'DAVT', 'HOVT', 'ICT', 'KRAT', 'THA', 'WIT'], 7],
	[['AWST', 'BDT', 'CHOT', 'CIT', 'CT', 'HKT', 'IRKT', 'MYT', 'PHT', 'SGT', 'SST', 'ULAT'], 8],
	[['WST', 'EIT', 'JST', 'KST', 'TLT', 'YAKT'], 9],
	[['AEST', 'CHST', 'CHUT', 'DDUT', 'PGT', 'VLAT'], 10],
	[['KOST', 'MIST', 'NCT', 'NFT', 'PONT', 'SAKT', 'SBT', 'SRET', 'VUT'], 11],
	[['FJT', 'GILT', 'MAGT', 'MHT', 'NZST', 'PETT', 'TVT', 'WAKT'], 12],
	[['PHOT', 'TKT', 'TOT'], 13],
	[['LINT'], 14],
	[['GMT', 'UTC', 'WET'], 0],
	[['AZOT', 'CVT', 'EGT'], -1],
	[['FNT', 'GST'], -2],
	[['ART', 'BRT', 'GFT', 'PMST', 'ROTT', 'UYT'], -3],
	[['AMT', 'AST', 'BOT', 'CLT', 'FKT', 'GYT', 'PYT', 'VET'], -4],
	[['ACT', 'COT', 'ECT', 'EST', 'PET'], -5],
	[['CST', 'EAST', 'GALT'], -6],
	[['MST'], -7],
	[['CIST', 'PST'], -8],
	[['AKST', 'GAMT', 'GIT'], -9],
	[['CKT', 'HST', 'TAHT'], -10],
	[['NUT'], -11],
	[['BIT'], -12])

	hour = 3600 #1 hour in seconds
	i = 0
	tz = ''
	offset = 0

	#store CLI args as variables
	time = int(args.time)
	time_format = args.timeformat
	#if no specified timezone, set UTC as the default
	if args.timezone is None:
		timezone = 'UTC'
	else:
		timezone = args.timezone

	# check inputted timezone against timezone tuple, if it is in the tuple then set the timezone and set the +/- offset
	for elem in timezones:
		for tz_list in timezones[i][0]:
			if timezone in tz_list:
				tz = timezone
				offset = timezones[i][1]
		i+=1

	#calculate the new time with difference calculated by hour x offset
	newtime = time + (hour * offset)

	#The print statement of Python2 has been replaced with the print () function in Python3
	#This requires any object to be wrapped in parenthesis for print output
	print(unixConverter(newtime, time_format, tz))

def unixConverter(timestamp, time_type, timezone):
	"""The unix_converter function uses the datetime library to convert the timestamp
	:parameter timestamp: An integer representation of a UNIX timestamp.
	:return: A human-readable date & time string."""

	date_ts = datetime.datetime.utcfromtimestamp(timestamp)
	#Use %H for 24 hour format, or %I with %p for 12 hour format with AM/PM
	#outputs the specified timeformat based on what the user entered
	if time_type == '24':
		return date_ts.strftime('%d-%m-%Y %H:%M:%S {}').format(timezone)
	else:
		return date_ts.strftime('%d-%m-%Y %I:%M:%S %p {}').format(timezone)

if __name__ == '__main__':
	main()
