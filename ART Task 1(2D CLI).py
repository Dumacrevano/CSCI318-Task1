import random
import math

# global variable for board size
# failure region is [xmin, xmax, ymin, ymax]
screen_size = [200,200]

# function to find distance between two points
def euclidean_distance(coor1, coor2):
	return math.sqrt((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)

def generate_coordinate(xlim, ylim):
        return [random.randint(0, xlim), random.randint(0, ylim)]

def check_collision(coor,failure_region):
    # checks for collision between coordinate and failure region
    if(coor[0] >= failure_region[0] and coor[0] <= failure_region[1] and coor[1] >=failure_region[2] and coor[1] <= failure_region[3]):
        return True

# function to run a trial between ART and RT returns a list of bool
def trial(failure_percentage, number_of_candidate = 10):
	steps = 0

	# generate first point
	first_point = generate_coordinate(screen_size[0], screen_size[1])
	
	# generate failure region
	total_screen_size = screen_size[0] * screen_size[1]
	total_failure_size = total_screen_size * failure_percentage
	failure_size = round(math.sqrt(total_failure_size))
	failure_coor = generate_coordinate(screen_size[0] - failure_size, screen_size[1] - failure_size)
	failure_region = [failure_coor[0], failure_coor[0] + failure_size, failure_coor[1], failure_coor[1] + failure_size]

	#print("Failure region" + str(failure_region))

	# initializing RT variables
	RT_point = first_point
	RT_flag = True
	RT_steps = 0

	# initializing ART variables
	ART_point = first_point
	ART_flag = True
	ART_steps = 0
	prev_points = []



	while RT_flag and ART_flag:
		steps += 1
		msg_string = "Step " + str(steps) + " "

		# RT part
		if(RT_flag):
			#print("RT:" + str(RT_point))

			# end condition for RT
			if(check_collision(RT_point, failure_region)):# is in region
				RT_flag = False
				RT_steps = steps
				msg_string += "RT - HIT "

			else:

				# generate next point
				RT_point = generate_coordinate(screen_size[0], screen_size[1])
				msg_string += "RT - MISS "

		# ART part
		if(ART_flag):
			#print("ART:" + str(ART_point))
			# end condition for ART
			if(check_collision(ART_point, failure_region)):# is in region
				ART_flag = False
				ART_steps = steps
				msg_string += "ART - HIT"

			else:
				msg_string += "ART - MISS"
				prev_points.append(ART_point)

				# find new candidates
				candidates = []
				for i in range(0, number_of_candidate):
					candidates.append(generate_coordinate(screen_size[0], screen_size[1]))
				# print(candidates)
				# initialize variables
				potential_candidate = []
				min_dist = math.inf
				max_dist = -math.inf

				# loop through candidates to find ideal candidate
				for i in candidates:
					# reset min distance
					min_dist = math.inf

					# loop through previous points and compare distance to find min distance
					for j in prev_points:
						dist = euclidean_distance(i,j)
						# print("dist: " + str(dist))
						
						# compare distance between candidate and previous points
						if dist < min_dist:
							min_dist = dist
						# print("min dist: " + str(min_dist))

					# compare distance between candidate to find max distance
					if min_dist > max_dist:
						potential_candidate = i
						max_dist = min_dist
						# print("max dist: " + str(max_dist))

				ART_point = potential_candidate
		print(msg_string)



	return [RT_flag, ART_flag]

def main(trial_amount, failure_percentage, number_of_candidate = 10):

	# initial variables
	current_trial = 0
	art_score = 0
	rt_score = 0
	tie_score = 0


	# main loop
	while trial_amount > current_trial:
		current_trial += 1

		print("Trial " + str(current_trial))

		result = trial(failure_percentage, number_of_candidate)

		if(result[0] == False and result[1] == False):
			tie_score += 1
		elif(result[0] == False):
			rt_score += 1

		else:
			art_score += 1

	print("RT: " + str(rt_score))
	print("ART: " + str(art_score))
	print("Tie: " + str(tie_score))

main(1000,0.01)