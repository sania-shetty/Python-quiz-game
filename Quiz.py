print("Welcome to my computer Quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay!! Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does GPU stand for?  ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PS stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got "+str(score)+" questions correct!")
print("You got "+str((score/5)* 100) +"%.")