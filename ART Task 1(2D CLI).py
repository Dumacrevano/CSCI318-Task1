import random
import math

# global variable for board size
screen_size = [10,10]

# function to find distance between two points
def euclidean_distance(coor1, coor2):
	return math.sqrt((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)

def generate_coordinate():
	return [random.randint(1, screen_size[0]), random.randint(1,screen_size[1])]

# function to run a trial between ART and RT
def trial(failure_percentage):
	steps = 0

	# generate first point
	first_point = generate_coordinate()
	failure_coor = generate_coordinate()
	print("Failure coor" + str(failure_coor))

	# initializing RT variables
	RT_point = first_point
	RT_flag = True
	RT_steps = 0

	# initializing ART variables
	ART_point = first_point
	ART_flag = True
	ART_steps = 0
	prev_points = []

	while RT_flag or ART_flag:
		steps += 1

		# RT part
		if(RT_flag):
			print("RT:" + str(RT_point))

			# end condition for RT
			if(RT_point == failure_coor):# is in region
				RT_flag = False
				RT_steps = steps

			else:

				# generate next point
				RT_point = generate_coordinate()

		# ART part
		if(ART_flag):
			print("ART:" + str(ART_point))
			# end condition for ART
			if(ART_point == failure_coor):# is in region
				ART_flag = False
				ART_steps = steps

			else:
				# find new candidate by generating 3 candidates
				prev_points.append(ART_point)
				candidates = [generate_coordinate(), generate_coordinate(), generate_coordinate()]

				# initialize variables
				potential_candidate = []
				min_dist = math.inf
				max_dist = -math.inf

				# loop through candidates to find ideal candidate
				for i in candidates:

					# loop through previous points and compare distance
					for j in prev_points:
						dist = euclidean_distance(i,j)
						
						# compare distance between candidate and previous points
						if dist < min_dist:
							min_dist = dist

					# compare distance between candidate
					if min_dist > max_dist:
						potential_candidate = i

				ART_point = potential_candidate



	return [RT_steps, ART_steps]

def main():

	# user input variables
	trial_amount = 100
	failure_percentage = 0.01

	# initial variables
	current_trial = 0
	art_score = 0
	rt_score = 0
	tie_score = 0


	# main loop
	while trial_amount > current_trial:
		current_trial += 1

		print("Trial " + str(current_trial))

		result = trial(failure_percentage)

		if(result[0] > result[1]):
			art_score += 1
		elif(result[0] < result[1]):
			rt_score += 1
		else:
			tie_score += 1

	print("ART: " + str(art_score))

	print("RT: " + str(rt_score))

	print("Tie: " + str(tie_score))

main()