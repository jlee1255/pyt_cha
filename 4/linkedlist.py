import requests
import re

def go_next(numbers):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(numbers)
    text = requests.get(url).text
    numbers = re.findall(r'\d+', text)
    if len(numbers) == 1:
        print(numbers[0])
        go_next(numbers[0])
    else:
        print(text)
    
loop = go_next("8022")