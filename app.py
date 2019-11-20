
correctAnswers = []
incorrectAnswers = []

# q1: The ground can be hard sometimes a1: true!
def question1():
    print("Type 0 for true ~ Type 1 for false !!")
    response = input("1. The ground can be hard sometimes: ")
    print("\n")
    correct_answer = ("0")
    if response == correct_answer:
        print("oh yomp!!!")
        correctAnswers.append('Question 1 was Correct')
        return 1    
    elif response != correct_answer:
        print("dang,,, that was true :^/. AND this was a free point! yikes pal")
        incorrectAnswers.append('Question 1 was Incorrect')
        return 0

# q2: Which color is the absolute best? a2: Green
def question2():
    print("\nPick a letter from a-f")
    response = input("2. Which color is the absolute best?: \n a. red \n b. orange \n c. yellow \n d. green \n e. blue \n f. purple")
    correct_answer = ("d")
    if response == correct_answer:
        print("ahahaAAAAAA yeaaahhhhhh baybee!")
        correctAnswers.append('Question 3 was Correct')
        return 1
    elif response != correct_answer:
        print("SHOOT! I guess our tastes don't allign. It's ok to be wrong sometimes")
        incorrectAnswers.append('Question 3 was Incorrect')
        return 0
# q3: How does one? a3: They just do
def question3():
    print("\nPick ANOTHER letter from a-d")
    response = input("3. How does one?: \n a. i dunno \n b. cry! \n c. two? \n d. they just do")
    correct_answer = ("d")
    if response == correct_answer:
        print("YO! How'd you guess that? Mad props LOL")
        correctAnswers.append('Question 3 was Correct')
        return 1
    elif response != correct_answer:
        print("HAHA I figured you'd miss this one... One free point, one stolen point, its fair.")
        incorrectAnswers.append('Question 3 was Incorrect')
        return 0
    
# q4: Hey cutie... what's your phone number ;^) ?? a4: any 10 digit input
def question4():
    print("Type 0 for true ~ Type 1 for false !!")
    response = input("4. My girlfriend is the cutest girl in the world: ")
    correct_answer = ("0")
    if response == correct_answer:
        print("oYeah! you know it!!")
        correctAnswers.append('Question 4 was Correct')
        return 1    
    elif response != correct_answer:
        print("yeah, you're absolutely incorrect but its whatever")
        incorrectAnswers.append('Question 4 was Incorrect')
        return 0

def question5():
    print("\nJust like, put in a number?")
    response = input("5. How old is Ruk: ")
=    correct_answer = ("19")
    if response == correct_answer:
        print("Oh HECK yeah buddy!!!!!")
        correctAnswers.append('Question 5 was Correct')
        return 1
    elif response != correct_answer:
        print("It's ok you didn't know")
        incorrectAnswers.append('Question 5 was Incorrect')
        return 0
        print("\n")
    
# results 
result = question1() + question2() + question3() + question4() + question5()
print("\n")

# print both lists
print("Your Results:")
for i in correctAnswers:
    print(i)
print("\n")
for i in incorrectAnswers:
    print(i)
print("\n")

# final message 
    # if correct answers >= 3, print ("oh yomp [name input], we VIBE ;^)")
if result >= 3:
    print(f"Ohhhh yomp!! You scored {result} out of 5, we vibe! ;^)")

else:
    print("Haha ok you're done with the quiz lol. You scored {result} out of 5")