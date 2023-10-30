# implement error handling

try:
    file = open('example.txt', mode='r')

except FileNotFoundError:
    file = open('example.txt', mode='w')