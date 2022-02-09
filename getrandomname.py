import requests
import json
from  random import randint


url = 'https://namey.muffinlabs.com/name.json?type=surname&frequency=RARE&count=10'
req = requests.get(url)
jsurnames = req.text
surnames = json.loads(jsurnames)

url = 'https://namey.muffinlabs.com/name.json?type=first&frequency=RARE&count=10'
req = requests.get(url)
fnames = req.text
firstnames = json.loads(fnames)

url = 'https://namey.muffinlabs.com/name.json?type=middle&frequency=RARE&count=10'
req = requests.get(url)
mnames = req.text
middlenames = json.loads(mnames)


a = randint(0,9)
b = randint(0,9)
c = randint(0,9)

print(firstnames[a])
print(middlenames[b])
print(surnames[c])





