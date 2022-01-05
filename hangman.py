
#The secret word the player is trying to guess
secretword = "JAMELA"
letterguessed = ""

#The number of turns before the player loses
failurecount = 6
#Loop until the player has mad too many failed attempts
#will break loop if they succeed instead
while failurecount > 0:
    #Get the guessed letter from the player
    guess = input ("Enter a letter: ")
    if guess in secretword:
        #Player guessed a correct letter!
        print(f"correct! There is one or more {guess} in the secret word. ")
    else:
        failurecount -= 1
        print(f"incorrect. There are no {guess} in the secret word. {failurecount} turn(s) left.")
    
    #maintain a list of all letters guessed
    letterguessed = letterguessed + guess
    Wronglettercount = 0

    for letter in secretword:
        if letter in letterguessed:
            print (f"{letter}, end= '")
        else:
            print ("_", end = "")
            Wronglettercount += 1
    #if there were no wrong letters, then the player won!
    if Wronglettercount == 0:
        print (f"congratulations! The secret word was {secretword}. You won!")
        break
    
else:
    print("sorry you lost. Try Agian!")