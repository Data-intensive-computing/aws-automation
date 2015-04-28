import boto
from boto.s3.key import Key
import numpy as np
import sys


def get_data():
	return np.array_str(np.random.randint(1000,100000,int(file_size)))


def main():
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	c = boto.connect_s3()
	b = c.get_bucket(bucket_name)
	k = Key(b)
	i = 0;	
	while i <= total_file_size: 
		k = Key(b)
		k.key = str(i)+"file.txt"
		data = get_data()
		k.set_contents_from_string(data)
		print 'uploaded file'
		size = sys.getsizeof(data)/1000 #bytes to kb
		if size == 0:
			i = i + 1
		else:
			i = i+ size


if __name__ == "__main__":
	if len(sys.argv) != 4:
		print 'usage python uploadFiles.py <bucket-name> <file-siz-in-kb> <total-file-size-in-kb>'
		exit()
	bucket_name = sys.argv[1]
	file_size   = sys.argv[2]
	total_file_size = sys.argv[3]
    	main()
