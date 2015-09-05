# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def load_hotels_data(N):
	hotels = {}
	for i in range(N):
		line = sys.stdin.readline().strip().split(" ")
		hotel_id = int(line[0])
		hotel_price = int(line[1])
		hotel_facilities = [str(facilitie) for facilitie in line[2:]]
		hotels[hotel_id] = {'price': hotel_price, 'facilities': hotel_facilities}
	return hotels

def load_customers_data(M):
	customers = {}
	for i in range(M):
		line = sys.stdin.readline().strip().split(" ")
		customer_budget = int(line[0])
		customer_requirements = [str(r) for r in line[1:]]
		customers[i] = {'budget': customer_budget, 'requirements': customer_requirements}
	return customers

def are_requirements_in_facilities(req,fac):
    # If 1 requirement is not satisfied, then the hotel is not valid.
    for i in range(len(req)):
    	if req[i] not in fac:
    		return False
    # There isn't unsatisfied requirements.
    return True 

def main():
	N = int(sys.stdin.readline().strip())
	hotels = load_hotels_data(N)
	M = int(sys.stdin.readline().strip())
	customers = load_customers_data(M)
	sorted_hotels = sorted(hotels, key=lambda k: len(hotels[k]['facilities']), reverse=True)
	for ckey, cvalue in customers.iteritems():
		hotels_match = []
		for hkey, hvalue in hotels.iteritems():
			if cvalue['budget'] >= hvalue['price']:
				if are_requirements_in_facilities(cvalue['requirements'], hvalue['facilities']):
					hotels_match.append(hkey)
		if len(hotels_match) == 0:
			sys.stdout.write('\n')
		else:
			# append hotels, already sorted by amount of facilities
			output = ""
			for i in sorted_hotels:
				if i in hotels_match:
					output = output + " " + str(i)
			sys.stdout.write(output.strip() + "\n")


if __name__ == '__main__':
	main()