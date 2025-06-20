# Harry Potter Code- Question number 1

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

question_1 = int(input("Do you like Dawn or Dusk? (1 - Dawn / 2 - Dusk)"))

if question_1 == 1:
    gryffindor += 1
    ravenclaw += 1

elif question_1 == 2:
    hufflepuff += 1
    slytherin += 1

else:
    print("Wrong input.")

# Question Number 2:

question_2 = int(input("When i'm dead, i want people to remember me as:"))

if question_2 == 1:
    hufflepuff += 2

elif question_2 == 2:
    slytherin += 2

elif question_2 == 3:
    ravenclaw += 2

elif question_2 == 4:
    gryffindor += 2

else:
    print("Wrong input")

# Question Number 3:

question_3 = int(input("Which kind of instrument most pleases you ear?:"))

if question_3 == 1:
    slytherin += 4

elif question_3 == 2:
    hufflepuff += 4

elif question_3 == 3:
    ravenclaw += 4

elif question_3 == 4:
    gryffindor += 4

else:
    print("Wrong input.")

print("🦁 Gryffindor:", gryffindor)
print("🦅 Ravenclaw:", ravenclaw)
print("🦡 Hufflepuff:", hufflepuff)
print("🐍 Slytherin:", slytherin)
