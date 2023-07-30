'''
This is a hangman game code in which there is a word store in a variable and the player have to guess the word
the player gets chaces until the hangman picture gets completed
'''

stages = ["    ",
          "______________",
          "               ",
          "              |",
          "              |",
          "              |",
          "              o",
          "             /|\ ",
          "              | ",
          "             / \ " ,
          "                   "]

word=input("Give a Word :")
lst = list(word)
lst2 = list(len(lst)*"-")

i=1
while(i<=len(stages)):
    a = input("Guess the letter : ")
    if a in lst:
        b=lst.index(a)
        lst2[b]=a
        print(lst2)
        if lst == lst2 :
            print("Congratulation you guessed it correctly")
            lst2.clear()
            lst2=list(len(lst)*"-")
            i=1
            q=input("Do you want to continue (y/n) :")
        else:
            continue
    else :
        print("\n".join(stages[0:i]))
        if i==len(stages):
            print("Sorry Try again next time")
            q = input("Do you want to continue (y/n) :")
            i=1
            lst2.clear()
            lst2=list(len(lst)*"-")
        else:
            i = i + 1
            continue
    if q == "y":
        lst2.clear()
        lst2=list(len(lst)*"-")
        i=1
        continue
    else:
        break


