import sys

number = 3
if len(sys.argv) == 2:
    number = int(sys.argv[1])
for i in range(number):
    print('Hello Python')