import requests
import json
from timeit import default_timer as timer
from datetime import timedelta

# open json file
file = open('values.json')

prime_numbers = []
json_data = json.load(file)
counter = 0

# time start
start = timer()
for data in json_data:
    # getting values 
    start = data[0]
    end = data[1]
    # connect to API
    request = requests.get(f"http://localhost:8080/primes?start={start}&end={end}")
    prime_numbers.append(request.json())

end = timer()
# wypisz czas dzialania
print('Executing script time: ', timedelta(seconds=end-start))

# save results to json file
prime_numbers_json = json.dumps(prime_numbers)
with open('output.json','w') as outfile:
    outfile.write(prime_numbers_json)

