natoAlphabet = ["Alfa",
"Bravo",
"Charlie",
"Delta",
"Echo",
"Foxtrot",
"Golf",
"Hotel",
"India",
"Juliett",
"Kilo",
"Lima",
"Mike",
"November",
"Oscar",
"Papa",
"Quebec",
"Romeo",
"Sierra",
"Tango",
"Uniform",
"Victor",
"Whiskey",
"Xray",
"Yankee",
"Zulu"]

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
        elif gamemode == "quit":
            break
        else:
            print("Try again")

def learnMode():
    while True:
        currentLetter = input("Enter a letter, RETURN to the main menu, or QUIT: ").upper()
        if currentLetter == "QUIT":
            print("Goodbye")
            # Return True to signal main() that it should exit its loop
            return True
        elif currentLetter == "RETURN":
            print("Goodbye")
            break
        i = 0
        answer = ""
        while i < 26:
            if natoAlphabet[i][0]==currentLetter:
                answer = natoAlphabet[i]
                break
            else:
                i += 1
        if answer == "":
            print("No corresponding code found. Try another letter.")
        else:
            print(answer)
    

if __name__ == "__main__":
    main()