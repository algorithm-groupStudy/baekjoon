import sys
sys.stdin = open("/Users/hyunwoochoi/Desktop/python/sample_input.txt")
input = sys.stdin.readline

def find_generator(numbers):
    total_sum = 0
    total_sum += numbers
    numbers = str(numbers)
    for number in numbers:
        total_sum += int(number)
    return total_sum

number = int(input())
min_number = number
for i in range(1, number):
    if find_generator(i) == number and min_number > i :
        min_number = i
if min_number == number:
    min_number = 0

print(min_number)

