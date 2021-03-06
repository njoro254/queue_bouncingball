from random import randint as r

import pandas as pd

def simulate_queue(arr1,arr2,ser1,ser2):
	#declare all variables
	arrival_time, idle_time, start_service, service_time, depart_time=0,0,0,0,0
	list1=[]



	# for each customer
	for i in range(1009):
		dictrow = {}
		# arrived at default time
		dictrow ['arrival_time'] = arrival_time

		#service started when the last patient left
		try:
			start_service = list1[-1]['depart_time']
			# dictrow ['start_service'] = start_service
		except:
			start_service = 0
			# dictrow ['start_service'] = start_service


		# they left after a random service time service may take upto 15 minutes
		# service_times = r(ser1,ser2)

		# combined  congruential function
		# (randomized large number modulus random number in between estimated minimum and estimated maximum service times)minus(randomized large number modulus random number in between estimated minimum and estimated maximum service times))modules estimated maximum service time
		service_times =((r(10000,10000000)%r(ser1,ser2)) -(r(10000,10000000)%r(ser1,ser2)))%ser2

		depart_time = start_service + service_times
		


		# dictrow['depart_time'] = depart_time

		# the difference between the time waited before the last consumer left
		try:
			idle_time = list1[-1]['depart_time'] - arrival_time
			# dictrow ['idle_time'] = idle_time
		except:
			idle_time = 0
			dictrow ['idle_time'] = 0

		#columns in order
		dictrow ['idle_time'] = idle_time
		dictrow ['start_service'] = start_service
		dictrow ['service_time'] = depart_time - start_service
		dictrow['depart_time'] = depart_time

		list1.append(dictrow)

		# calls come every 10 minutes
		# arrival_time += r(arr1,arr2)

		# linear congruential function
		# form of random_value = (randomized large number * estimated minimum arrival time + estimated maximum arrival time) modulues maximum estimated arrival time
		arrival_time = (r(0,1000)*arr1 + arr2)%arr2



	#get averages for idle and service
	average_idle_time, average_service_time = 0,0

	for items in list1:
		average_idle_time += items['idle_time']
		average_service_time += items['service_time']

	average_idle_time = average_idle_time/1000
	average_service_time = average_service_time/1000


	# save data type unformatted in json
	with open ('waitlist.json', 'w+') as f:
		f.write(str(list1))

	df = pd.DataFrame.from_dict(list1)
	df.to_csv (r'waitlist.csv', index = False, header=True)

	with open ('waitlist.csv', 'a') as f:
		f.write(str({'average_idle_time':average_idle_time, 'average_service_time':average_service_time}))

	return average_idle_time, average_service_time

