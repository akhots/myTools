print('CompareList v.0.1\r\n')

sourceList = []
compareList = []
resultList = []

print('Enter source list')
element = 'begin'

while element != '':
	element = input(': ')
	if element != '':
		sourceList.append(element)
# ----------------------------------------------------------------

print('\r\nEnter compare list')
element = 'begin'

while element != '':
	element = input(': ')
	if element != '':
		compareList.append(element)
# ----------------------------------------------------------------

print('Results:\r\n')

for one in sourceList:
	if one in compareList:
		resultList.append(one + ' - OKAY')
	else:
		resultList.append(one + ' - No')

for one in resultList:
	print(one)

input('\r\nDone!\r\n\r\nPress Enter to exit...')
