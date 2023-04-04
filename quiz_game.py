print("Welcome to my computer quiz")
score = 0

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("")
print(score)