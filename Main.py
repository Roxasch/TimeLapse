import os
import time

save_path = '/Users/Kyle/Documents/Programming/Projects/Python/TimeLapse/Test/'
time_gap  = 4

os.system("echo 'starting'")

def max(path):
    result = 0
    for root, dirs, files in os.walk(path):
    	for name in files:
    		if name[-4:] == '.jpg':
	        	if int(name[:-4]) > result:
	        		result = int(name[:-4])
    return result

if __name__ == "__main__":
	i = max(save_path)

	while True:
		i = i + 1
		os.system("screencapture -t jpg -x %s%d.jpg" % (save_path, i))
		print 'saving %d.jpg' % i
		time.sleep(time_gap)
