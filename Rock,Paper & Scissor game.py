import random
def get_user_choice():
    # Getting the user choice or input
    x = input("Enter your choice (rock, paper, scissors): ")
    while x=="rock" or x=="paper" or x=="scissor":
        return x
    else:
        return "invalid input, please enter rock paper or scissor "

 
    
def get_computer_choice():
    
    # Getting computer choice 
    
    return random.choice(["rock","paper","scissor"])
    
    
def result(x,computer_choice):    
    
    # Calculating result on the basis of user and computer choice 
    
    if x==computer_choice:
        return "match is tie !"
    elif (x=="rock" and computer_choice=="scissor") or (x=="paper" and computer_choice=="rock") or (x=="scissor" and computer_choice=="paper"):
        return " you win 🏆"
        
    else:
        return "you lost and computer wins "
        
def main():
    
    # Main function to run the program 
    
    print ( " welcome to the game ")
    x=get_user_choice()
    computer_choice=get_computer_choice()
    print(f"\nyou choose : ",{x})
    print(f"\ncomputer choose: ",{computer_choice})
    winner=result(x,computer_choice)
    print(f"\n{winner}")
    
    # The line if __name__ == "__main__": is a common Python idiom used to determine whether a Python script is being run as the main program or if it is being imported into another module.
        
if __name__=="__main__":
    main()

