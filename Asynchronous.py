import aiohttp
import asyncio
import json
from timeit import default_timer as timer
from datetime import timedelta

# open json file
file = open('values.json')

prime_numbers = []
json_data = json.load(file)
counter = 0

async def main():
    async with aiohttp.ClientSession() as session:
        for data in json_data:
            # getting values
            start = data[0]
            end = data[1]
            # Connect to API
            async with session.get(f"http://localhost:8080/primes?start={start}&end={end}") as resp:
                wynik = await resp.json()
                prime_numbers.append(wynik)

# time start
start = timer()
asyncio.run(main())
end = timer()
# Execution time print
print('Execution time script: ', timedelta(seconds=end-start))

# save results to json
prime_numbers_json = json.dumps(prime_numbers)
with open('output.json', 'w') as outfile:
    outfile.write(prime_numbers_json)

