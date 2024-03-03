import re

file = open('ocr.txt', 'r')
lines = file.readlines()
 
for line in lines:
    line = re.sub('[^A-Za-z0-9]+', '', line)
    if len(line.strip()) > 0 :
        print(line)