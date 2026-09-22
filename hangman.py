import random
list_words = ["banana", "apple", "mango"]
word = random.choice(list_words)
xword = list(word)
print("""Welcome to hangman, you have to guess the word to win.
You can make only 6 mistakes, otherwise you are out. 
You can write only one letter per guess, good luck! 
Hint: The word is a fruit ;)
""")
chances = 6
xHidden = []
guessed = []
for i in range(0,len(xword)):
    xHidden += "_"
print(f'the word has {len(xHidden)} letters')

display = ""

for letter in range(len(xHidden)):
    display += "_ "
            
print(display)
while(chances>0):
    a = input("type a letter: ").lower()
    
    if len(a) != 1 or not a.isalpha():
        print("you have to enter a singular letter")
        print(display)
        continue
        #a = input().lower()
        
    if a in xHidden:
        print("you have already guessed that letter")
        print(display)
        continue
        #a = input().lower()
        
    if a in xword:
        for i in range(0,len(xword)):
            if a == xword[i]:
                xHidden[i] = a
                guessed.append(a)
                #print(guessed)
    else:
        print(f"try again, you have {chances-1} left")    
        chances -= 1
    
    display = ""

    for letter in range(len(xHidden)):
        if xHidden[letter] in guessed:
            display += xHidden[letter] + " "
        else:
            display += "_ "
            
    print(display)
    #print(xHidden)
    if xHidden == xword:
        break
if xHidden == xword:
    print(f"you guessed right! :D")
else:
    print("you guessed wrong :/")
    print(f"the word was {word}")