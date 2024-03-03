import requests
import zipfile
import io
import re

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
response = requests.get(url)

def read_comment(filename):
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        with zip_ref.open(filename, 'r') as file:
            contents = file.read().decode('utf-8')
            return zip_ref.getinfo(filename).comment.decode('utf-8'), contents

def go_next(filename):
    comment, contents = read_comment(filename)
    if comment.isalpha():  # Check if comment consists of alphabets
        print(comment, end='')
    numbers = re.findall(r'\d+', contents)
    if numbers:  # Check if any numbers are found in the contents
        next_filename = str(numbers[0]) + ".txt"
        go_next(next_filename)

go_next("90052.txt")