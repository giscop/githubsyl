import os

def mount_details():
	if os.path.exists('/proc/mounts'):
		df = open('/proc/mounts')
		for line in df:
			line = line.strip()
			words = line.split()
			print('{} on {} type {}'.format(words[0],words[1],words[2]), end=' ')
			if len(words) > 5:
				print('({})'.format(' '.join(words[3:-2])))
			else:
				print()
		df.close()
		
if __name__ == '__main__':
	mount_details()
	