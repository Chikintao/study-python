def calculate_average(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

def find_max(numbers):
    max_number = 0
    for i in numbers:
        if(max_number < i):
            max_number = i
    return max_number