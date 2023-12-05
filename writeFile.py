file1 = 'hello.txt'
file2 = 'hello1.txt'
with open(file1, 'r') as source_file:
    data = source_file.read()
with open(file2, 'w') as destination_file:
    destination_file.write(data)