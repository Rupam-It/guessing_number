import random
limit=10
def display_titel():
    print("\n!!!!guess correct the number!!!")
    print()
def play_game():
    number=random.randint(1,limit)
    print("I'M thinking of a number of from 1 to "+ str(limit)+"\n")
    count=1
    while True: 
        guess=int(input("your guess : "))
        if guess <number:
            print("too low !")
            count+=1
        elif guess >number :
            print("too high !")
            count+=1
        elif guess == number :
            print("Woo! you guess it in "+str(count)+" tries\n")
            return 
def main():
    display_titel()
    again='y'
    while again.lower()=='y':
        play_game()
        again=input("would you like to play again? (y/n): ")
        print()
    print("game over!")
if __name__== "__main__":
    main()