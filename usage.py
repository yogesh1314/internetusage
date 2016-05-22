import os, time

a = time.localtime()
year = str(a.tm_year)
month = str(a.tm_mon)
day = str(a.tm_mday)

def saveusagehelper(rx, tx):
	if os.path.exists('usage'):
		f = open('usage','r')
		x = f.readlines()
		#print x
		#print x[0].strip()[4:]
		#print x[1].strip()[4:]
		rx = rx+int(x[0].strip()[4:])
		tx = tx+int(x[1].strip()[4:])
		write_str = "rx: "+str(rx)+"\n"+"tx: "+str(tx)+"\n"
		#print write_str
		#print "\n"
		f.close()
		f = open('usage','w')
		f.write(write_str)
		f.close()
	else:
		f = open('usage','w')
		write_str = "rx: "+str(rx)+"\n"+"tx: "+str(tx)+"\n"
		f.write(write_str)
		f.close()

def saveusage(inf_name, rx, tx):
	os.chdir(inf_name)
	if not os.path.exists(year):
		os.makedirs(year)
	os.chdir(year)
	if not os.path.exists(month):
		os.makedirs(month)
	os.chdir(month)
	if not os.path.exists(day):
		os.makedirs(day)
	os.chdir(day)
	saveusagehelper(rx,tx)
	os.chdir('..')
	saveusagehelper(rx,tx)
	os.chdir('..')
	saveusagehelper(rx,tx)
	os.chdir('..')

def getusage():
	f = open("/proc/net/dev","r")
	l = f.readlines()
	f.close()
	l.pop(0)
	l.pop(0)
	for i in l:
		k = i.split()
		if k[0] != 'lo:':
			inf_name = k[0]
			inf_name = inf_name[:-1]
			rx = int(k[1])
			tx = int(k[9])
			if not os.path.exists(inf_name):
				os.makedirs(inf_name)
			saveusage(inf_name, rx, tx)
			os.chdir('..')
xyz = 20;
while(xyz):
	getusage()
	xyz = xyz - 1
	time.sleep(10)
