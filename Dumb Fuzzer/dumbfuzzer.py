# png generation source
# https://www.jasonshah.com/a-python-script-to-generate-a-random-fuzzy-image/

# time and date source
# https://www.programiz.com/python-programming/datetime/current-datetime

import os
from PIL import Image
import png
import numpy
from datetime import datetime
import math
import shutil
import cv2
import test2


# algorithm options
number_of_candidate = 10



now = datetime.now()
foldername = now.strftime("%d_%m_%Y %H-%M-%S")

# filename = "sed crocs cat.png"
filename = input("Please enter seed file name:")

# get program name to test
program_name = input("Please enter program name:")
# program_name = "imageconv.py"

# get trials input
trials = int(input("How many trials?"))
# trials = "4"
trials = int(trials)

# ask if user want to delete sample picture results
result = input("Delete results that return correct output?(Y/N)")
# result = "Y"

if(result.upper() == "YES" or result.upper() == "Y"):
	del_flag = True
else:
	del_flag = False

# check if sample pictures folder exists
if not os.path.exists(foldername):
	# create folder
    os.mkdir(foldername)

# check if temp pictures folder exists
if not os.path.exists("temp"):
	# create folder
    os.mkdir("temp")

# initialize lists
tested_pictures = []
candidates = []
sample_errors = []

# trial 1
trial_num = 1
tested_pictures.append(filename)
os.system("python " + program_name + " " + "\"" + filename + "\"")

# verify trial 1
output_filename = filename.replace("png", "jpg")
img = Image.open(output_filename)
result_format = img.format
print("Trial 1:")
print("Output file format is: " + result_format)

# get dimensions of seed
x, y = img.size

if(x == 1 and y == 1):
	trial_num = trials
	print("Seed image can not be 1x1")

del img

# main loop
while trial_num < trials:
	print("Trial " + str(trial_num+1) + ":")

	# generate candidates
	for i in range(number_of_candidate):
		
		# generate png file
		filename =  "temp/candidate" + str(i + 1) + ".png"
		l = []
		for i in range(0, y):
		    l.append(numpy.random.randint(0,255,x*3).tolist())
		png.from_array(l, "RGB").save(filename)
		candidates.append(filename)

	# initialize variables
	potential_candidate = ""
	min_dist = math.inf
	max_dist = -math.inf

		# loop through candidates to find ideal candidate
	for i in candidates:
		# reset min distance
		min_dist = math.inf
		imageB = i

		# loop through previous images and compare distance to find min distance
		for j in tested_pictures:

			imageA = j

			feature_dist = test2.image_feature_compare(imageA,imageB)
			color_dist=test2.image_color_difference(imageA,imageB)
			dist=(feature_dist+color_dist)/2
			
			# compare distance between candidate and previous points
			if dist < min_dist:
				min_dist = dist
			# print("min dist: " + str(min_dist))

			del imageA

		# compare distance between candidate to find max distance
		if min_dist > max_dist:
			potential_candidate = i
			max_dist = min_dist
			# print("max dist: " + str(max_dist))

		del imageB

	filename = foldername + "/sample" + str(trial_num + 1) + ".png"
	os.rename(potential_candidate,filename)
	
	
	tested_pictures.append(filename)

	# run program
	os.system("python " + program_name + " " + "\"" + filename + "\"")

	#verify
	output_filename = filename.replace("png", "jpg")
	
	try:
		img = Image.open(output_filename)
		result_format = img.format
		print("Output file format is: " + result_format)
		del img

		if(result_format != "JPEG"):
			sample_errors.append(filename)

		# delete if result is correct and delete flag is true
		if(del_flag == True and result_format == "JPEG"):
			os.remove(output_filename)
			# os.remove(filename)
	except:
		print("Error in trial:" + str(trial_num))
		sample_errors.append(filename)
	
	trial_num = trial_num + 1

# delete temp folder and its contents
shutil.rmtree("temp")

print("Samples that does not result in JPEG:")
print(sample_errors)

input("press enter to quit")