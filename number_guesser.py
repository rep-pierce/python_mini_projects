import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Must be larger than 0")
        quit()
else:
    print("Must be a number")
    quit()

random_number = random.randint(0, top_of_range)
guess_times = 0
print

while True:
    str_answer = input(f"Guess number from 0 to {top_of_range}! ")
    
    if str_answer.isdigit():
        answer = int(str_answer)
    else:
        print("Must be a number")
        continue

    if answer == random_number:
        guess_times += 1
        break
    elif answer > random_number: 
        print("Answer is lower")
        guess_times += 1
    else:
        print("Answer is higher")
        guess_times += 1

print(f"It took you {guess_times} guesses to get the right answer")