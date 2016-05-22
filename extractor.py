import os, time, sys
def infList():
	inf_list = []
	dirs = os.listdir('.')
	for d in dirs:
		if os.path.isdir(d):
			inf_list.append(d)
	return inf_list

def formatted(x):
	x = int(x)
	size = ''
	i = 0
	while x > 1024:
		x = x/1024
		i = i + 1
	if i == 0:
		size = ' Bytes'
	elif i == 1:
		size = ' KB'
	elif i == 2:
		size = ' MB'
	elif i == 3:
		size = ' GB'
	elif i == 4:
		size = ' TB'
	return str(x)+size

def sterile(num):
	try:
		if int(num) < 10:
			return str(num[1:])
		else:
			return str(num)
	except ValueError:
		print 'Enter data in yyyy dd mm form only. No Strings allowed.\nTry Again.'
		sys.exit()
	
def extractusage(year, month, day):
	inf_list = infList()
	if year == '':
		print 'try $python extractor.py --help'
		return
	try:
		for i in inf_list:
			level = 0
			os.chdir(str(i))
			level = level + 1
			os.chdir(year)
			level = level + 1
			if month != '':
				os.chdir(month)
				level = level + 1
			if day != '':
				os.chdir(day)
				level = level + 1
			f = open('usage','r')
			c = f.readlines()
			f.close()
			rx = c[0].strip()[4:]
			tx = c[1].strip()[4:]
			print '\nInterface '+str(i)+' :'
			print 'Receieved Data: '+formatted(rx)+''
			print 'Transmitted Data: '+formatted(tx)+''
			while(level > 0):
				os.chdir('..')
				level = level - 1
	except OSError:
		print 'No Usage Data is available for this input\nTry Again'
#24/01/2016
#2016/01/24
#2016/1/1
#python extracter.py 2016 01 02 (yyyy mm dd)
year = ''
month = ''
day = ''
try:
	if sys.argv[1] == '--help':
		print 'Enter your command in specified format to extract usage:\n"$ python extractor.py yyyy mm dd"\n' 
		print '"$ python extractor.py yyyy" will yield usage for that year.' 
		print '"$ python extractor.py yyyy mm" will yield usage for given month in given year'
		print '"$ python extractor.py yyyy mm dd" will yield usage for given day in given month in given year'
		print 'Results will be printed for all interfaces used by device'
		sys.exit()
	if sys.argv[1] != None:
		year = str(sys.argv[1])
	else: 
		year = ''
	if sys.argv[2] != None:
		month = sterile(sys.argv[2])
	else:
		month = ''
	if sys.argv[3] != None:
		day = sterile(sys.argv[3])
	else:
		day = ''
except IndexError:
	pass
extractusage(year, month, day)	