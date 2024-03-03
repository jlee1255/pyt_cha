import requests
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
response = requests.get(url)
data = pickle.loads(response.content)

for list in data:
    for char, count in list:
        print(char * count, end='')
    print()