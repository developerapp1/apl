import os

for filename in os.listdir():
    if os.path.isfile(filename):
        print(filename)