
import nltk #Natural Language Toolkit proivdes access to the World Corpus which is an extensive list of English words 
nltk.download('words', quiet=True)
from nltk.corpus import words

word_set = set(words.words())

print("-------------Welcome to the Word Switch Game-------------")
print("Rules: Enter a word then type it spelled backwards")
print("The reversed word must also be a real word")

points = 0

playing = True

while playing:
    word = str(input("Enter a word with less than 10 characters:"))
    if len(word) >= 10:
        print("Word is too long, try again:")
        continue #continue jumps back to the top of the while loop

    palindrome = (word[::-1])
    print(f"The palidrome of the word the you have inserted {word} is {palindrome}")
    if palindrome in word_set:
        print(f"The palindrome, {palindrome},  is a valid English word")
        print("Congra Congra, You have earned 500 points")
        points = points + 500

        current_points = str(input("Would you like to see how many points you currently have:"))
        if current_points == "yes":
            print(f"You have {points} points!!!")
        elif current_points == "no":
            print("Okay, let's proceed!")

        replaying = True
        while replaying:
            replay = str(input("Play Again? (yes/no):"))
            if replay == "no":
                playing = False
                print("Thanks for playing, please come back again")
                break
            elif replay != "yes":
                print("Please type yes or no (lowercase):")
                continue
            else:
                replaying = False
                continue
    else:
        print(f"The palindrome{palindrome} is not a valid English word")
        print("Unfortunately you have lost 100 points")
        points = points - 100

        current_points = str(input("Would you like to see how many points you currently have:"))
        if current_points == "yes":
            print(f"You have {points} points!!!")
        elif current_points == "no":
            print("Okay, let's proceed!")

        replaying = True
        while replaying:
            replay = str(input("Play Again? (yes/no):"))
            if replay == "no":
                playing = False
                print("Thanks for playing, please come back again")
                break
            elif replay != "yes":
                print("Please type yes or no (lowercase):")
                continue
            else:
                replaying = False
                continue
