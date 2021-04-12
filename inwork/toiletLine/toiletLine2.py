
import random

people = 10
toilets = 2

workDayTime = 540
toilTime = 20

days = 100
experiments = 10


#peoplTimeList = []
#
#for man in range(people):
#	peoplTimeList.append(random.randint(0,workDayTime-toilTime))
#
#collision = 0
#for monent in range(workDayTime):
#	count = 0
#	for peoplTime in peoplTimeList:
#		if monent >= peoplTime  and monent < peoplTime + toilTime:
#			count = count + 1
#	if count > toilets:
#		collision = collision + 1
#
#print(str(workDayTime) + ' - ' + str(collision))



for exper in range(experiments):
	collision = 0
	for day in range(days):
		peoplTimeList = []
		for man in range(people):
			peoplTimeList.append(random.randint(0,workDayTime-toilTime))
		for monent in range(workDayTime):
			count = 0
			for peoplTime in peoplTimeList:
				if monent >= peoplTime  and monent < peoplTime + toilTime:
					count = +=1
			if count > toilets:
				collision = +=1
	print(str(workDayTime*days).ljust(10) + str(collision).ljust(10) + str(collision/(workDayTime*days)))

#--------------------

import random

toilets = 1

workDayTime = 540
toilTime = 20

days = 100



def toilColl(people,toilets,workDayTime,toilTime,days):
	collision = 0
	for day in range(days):
		peoplTimeList = []
		for man in range(people):
			peoplTimeList.append(random.randint(0,workDayTime-toilTime))
		for monent in range(workDayTime):
			count = 0
			for peoplTime in peoplTimeList:
				if monent >= peoplTime  and monent < peoplTime + toilTime:
					count +=1
			if count > toilets:
				collision = +=1
	return collision/(workDayTime*days)

for ppp in range(100):
	print(str(ppp).ljust(10) + str(toilColl(ppp*toilets,toilets,workDayTime,toilTime,days)))

