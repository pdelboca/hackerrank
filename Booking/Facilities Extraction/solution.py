import sys

def get_facilities(N):
	facilities = []
	for i in range(N):
		fac = str(sys.stdin.readline().strip())
		facilities.append(fac)
	return facilities

def main():
	N = int(sys.stdin.readline().strip())
	facilities = get_facilities(N)
	description = str(sys.stdin.read().strip().lower())
	sorted_facilities = sorted(facilities)
	for fac in sorted_facilities:
		if fac.lower() in description:
			sys.stdout.write(fac+'\n')

if __name__ == '__main__':
	main()