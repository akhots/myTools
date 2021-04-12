
import random

people = 10

toilet = 1

wontToil = 0.05

tries = 10000
exper = 10

for one1 in range(exper):
	collision = 0
	for one2 in range(tries):
		getToil = 0
		for one3 in range(people):
			if random.random() <= wontToil:
				getToil = getToil + 1
		if getToil > toilet:
			#print('I can\'t get to the toilet!!! :(((')
			collision = collision + 1
	print('\r\nCollisions - ' + str(collision) + ' of ' + str(tries))



# -------------------------


import random


toilet = 1

wontToil = 0.05

tries = 10000


def toilColl(people,toilet,wontToil,tries):
	collision = 0
	for one in range(tries):
		getToil = 0
		for one in range(people):
			if random.random() <= wontToil:
				getToil = getToil + 1
		if getToil > toilet:
			#print('I can\'t get to the toilet!!! :(((')
			collision = collision + 1
	#print('\r\nCollisions - ' + str(collision) + ' of ' + str(tries))
	return collision/tries

for ppp in range(100):
	print(str(ppp).ljust(10) + str(toilColl(ppp*toilet,toilet,wontToil,tries)))

