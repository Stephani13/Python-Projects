## Author: Stephani Izquierdo (Tech Academy code)
##
##
##Purpose:  Creating a game with the Tech Academy.
##          
##

def start(nice=0, mean=0, name=""):
    #get user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    '''
        check if this is a new game or not
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    '''
    if name != "":
        print("\n Thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\n What is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game, you will be greeted \nby several different people.\nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop=False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick=input('\nA stranger approaches you for a conversation. Will you be nice \nor mean? (N/M) \n>>>: ').lower()
        if pick == 'n':
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == 'm':
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False


        pick2=input('\nA stranger approaches you to ask you for money. Will you be nice \nor mean? (N/M) \n>>>: ').lower()
        if pick2 == 'n':
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick2 == 'm':
            print("\nThe stranger glares at you \nsad and hungry and storms off...")
            mean = (mean + 1)
            stop = False


        pick3=input('\nA stranger approaches and ask you if you would \nlike what they are eating. Will you be nice \nor mean? (N/M) \n>>>: ').lower()
        if pick3 == 'n':
            print("\nThe stranger give you a litle...")
            nice = (nice + 1)
            stop = False
        if pick3 == 'm':
            print("\nThe stranger glares at you \ndisappointed and storms off...")
            mean = (mean + 1)
            stop = False
        

        pick4 = input('\nYou are in a bus and an old lady ask for your seat. Will you be nice \nor mean? (N/M) \n>>>: ').lower()
        if pick4 == 'n':
            print("\nThe stranger give you a litle...")
            nice = (nice + 1)
            stop = False
        if pick4 == 'm':
            print("\nThe stranger glares at you \ndisappointed and storms off...")
            mean = (mean + 1)
            stop = False


        pick5 = input('\nYou are walking to work and a man ask you \nwhat time is it.\nWill you be nice or mean? (N/M)\n>>>: ').lower()
        if pick5 == 'n':
            print("\nThe stranger give you a litle...")
            nice = (nice + 1)
            stop = False
        if pick5 == 'm':
            print("\nThe stranger glares at you \ndisappointed and storms off...")
            mean = (mean + 1)
            stop = False

        score(nice,mean,name) #passes the three variables to the score()


        

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the value stored within the 3 variables
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    #Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win!! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N): \n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("Enter (Y) for 'Yes', (N) for 'NO':\n>>>")



def lose(nice,mean,name):
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    again(nice,mean,name)




def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice we do not do anithing to the name since we dont wanna ask for the name again
    start(nice,mean,name)

























if __name__ =="__main__":
    start()
