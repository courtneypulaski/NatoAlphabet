import random

natoAlphabet = ["alfa",
"bravo",
"charlie",
"delta",
"echo",
"foxtrot",
"golf",
"hotel",
"india",
"juliett",
"kilo",
"lima",
"mike",
"november",
"oscar",
"papa",
"quebec",
"romeo",
"sierra",
"tango",
"uniform",
"victor",
"whiskey",
"xray",
"yankee",
"zulu"]

def main():
    while True:
        gamemode = input("Select a game mode - learn or guess, or quit: ").lower()
        if gamemode == "learn":
            print("This is learn mode")
            # If learnMode returns True it means the user asked to quit the program
            if learnMode():
                break
        elif gamemode == "guess":
            print("This is guess mode")
            if guessMode():
                break
        elif gamemode == "quit":
            break
        else:
            print("Try again")

def learnMode():
    while True:
        currentLetter = input("Enter a letter, RETURN to the main menu, or QUIT: ").lower()
        if currentLetter == "quit":
            print("Goodbye")
            # Return True to signal main() that it should exit its loop
            return True
        elif currentLetter == "return":
            print("Goodbye")
            break
        i = 0
        answer = ""
        while i < 26:
            if natoAlphabet[i][0]==currentLetter:
                answer = natoAlphabet[i].capitalize()
                break
            else:
                i += 1
        if answer == "":
            print("No corresponding code found. Try another letter.")
        else:
            print(answer)

def guessMode():
    while True:
        number = random.randint(0,25)
        answer = natoAlphabet[number]
        print(f"What is the corresponding code for the letter {answer[0].upper()}? ")
        guess = input("Type a word, or Return to main menu or Quit: ")
        if guess == answer:
            print("Correct, you win!")
        elif guess == "quit":
            print("Goodbye")
            return True
        elif guess == "return":
            print("Goodbye")
            break
        else:
            print(f"Incorrect, the answer was {answer.capitalize()}.")
    

if __name__ == "__main__":
    main()