FILE1 = '3/file1.txt'
FILE2 = '3/file2.txt'

with open(FILE1) as first_file:
    first = [int(num.replace('\n','')) for num in first_file.readlines()]
    
with open(FILE2) as second_file:
    second = [int(num.replace('\n','')) for num in second_file.readlines()]
    
result = [num for num in first if num in second]
print(result)