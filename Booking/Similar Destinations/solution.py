import sys
import itertools

def get_destinations():
	# london:theatre,museums,monuments,food,parks,architecture,nightlife
	destinations = {}
	for line in sys.stdin:
		fac = str(line.strip())
		city, tags = fac.split(':')
		tags = sorted(tags.split(','))
		destinations[city] = tags
	return destinations

def main():
	# THIS WILL EXPLODE IN PROCESSING TIME
	common_tags = int(sys.stdin.readline().strip())
	destinations = get_destinations()
	sorted_destinations = sorted(destinations.keys())
	
if __name__ == '__main__':
	main()