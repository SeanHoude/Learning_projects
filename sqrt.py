number = int(input("What number do you want to calc the sqrt for?: "))
possible_sqrt = float(input("What do you think the sqrt is?"))

tolerance = .001
attempts = 0

while possible_sqrt * possible_sqrt - number > tolerance or possible_sqrt * possible_sqrt - number < -tolerance:
    print(f"Attempt {attempts}: possible Square root is {possible_sqrt} top loop")
    possible_sqrt = (possible_sqrt + (number / possible_sqrt)) / 2
    attempts += 1

print(f"The square root of {number} is {possible_sqrt}")