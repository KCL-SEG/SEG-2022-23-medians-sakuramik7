"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        numbers.sort()
        if len(numbers) % 2 == 1:
            print(numbers[int((len(numbers)+1)/2)-1])
        else:
            num = numbers[int((len(numbers)-1)/2)]
            num2 = numbers[int((len(numbers)+1)/2)]
            a = (num + num2)/2
            print(a)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
