difficalty = input("Choose the difficulty level; Beginner, Medium, Hard? ")

if difficalty == "beginner":
    print("Here we go!!!!")
    question1 = input("1st.: What is the first animal domesticated by humans? ")
    if question1 == "dog":
        print("Correct!")
    elif question1 != "dog":
        print("No, The correct answer is dog.")