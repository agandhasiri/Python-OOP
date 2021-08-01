##################################################################
# Student contributions to the interest calculator
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#---------------------------------------------------------------------------------

def greeting():                                                   # need to write in print() to dislay the message, tripple quotes for the many lines message .    
    greet=print("""This interest calculator will ask you to select an interest rate,    
followed by a principal value.  It will then calculate and display
the principal, interest rate, and balance after one year.  You will then                 
be invited to execute the process again or terminate.""")
    return greet                                                                        

#---------------------------------------------------------------------------------

def getRate(choices):

    a=True
    while a:
        tuples_list = []                                                # a list for all the tuples of choices and its alphabetic order
        alpha_list = []
        print("\nPlease select an interest rate:")
        for j, i in enumerate(choices):                                 # numbering the choices
            print(f'{chr(65 + j)}){i:>3}%')                             # chr() converts integer to character, alphabets start from 65
            tuples_list.append((chr(65 + j), i))                        # append the choices and its given aplha numbering as tuple to a list
            alpha_list.append((chr(65 + j)))                            # append all the aplhabest for checking in to another list

        k=input(f'Enter {tuples_list[0][0]}-{tuples_list[-1][0]}: ')     # first aplhabet and last alphabet in the tuple list
        if k not in alpha_list:                                          # checking the input with alpha_list
            print("That is not a valid selection.")                      # if not present, gives the message and asks again

        for j in tuples_list:                                            # if input is in alpha_list, it goes to tuples_list
            if k == j[0]:                                                # checks with every first place with input in every tuple
                v= j[1]/100                                              # if finds, takes the second value from that tuple and converts and stores in v
                a=False                                                  # stops taking input after successful valid input

    return v                                                             # returns desired value as stored in v

#---------------------------------------------------------------------------------

def getPrincipal(limit):
    i=0
    while True :

        try:                                                                # try error checking 
            i=input(f'\nEnter the principal (limit {limit}): ').strip("$")    # take input as string and strip out the "$" symbol if given
            i=float(i)                                                      # convert it into float

            v=str(i).split(".")                                             # conevrt into string and split it with "."(decimal point) and store in v
            if not i<=int(limit):                                           # checking the i value with limit 
                print(f'The principal can be at most {limit}.')             # a message if its not in the limit
            if i<1:                                                         # checking if i is a negative integer
                print('You must enter a positive amount.')                   


            if 1<=i<=int(limit):                                            # if i is in limit
                if not len(v[-1])<=2:                                       # if decimal vaulues are more than two, repeat by giving a message
                    print("The principal must be specified in dollars and cents.")

                else:
                    j=f'{i:.2f}'                                             
                    break                                                   # (comes out of the loop) stops asking for input after successful valid input


        except ValueError:                                                  # a value error exception
            print("Please enter a number")

    return j
#---------------------------------------------------------------------------------

def computeBalance(principal, rate):

    principal=float(principal)                                             # convert the principle amt into a float value
    b=principal + ((principal) * rate)                                     # the formula for balance
 
    return  b

#---------------------------------------------------------------------------------

def displayTable(principal, rate, balance):
    principal = float(principal)                                           # convert the principle amt into a float value
    display=print(f'Initial Principal   Interest Rate   End of Year Balance\n{"="*55}\n${principal:<19.2f}{rate:<16.2f}${balance:.2f}')
    return display                                                         
#---------------------------------------------------------------------------------
#
def askYesNo(prompt):

    a=input(prompt)                                                       # ask for input
    if a[0] in ["y","Y"]:                                                 # if the first letter of the input is in the list (a list of strings which represents "yes")
        active=True                                                       # it starts asking questions again from interest rate for computation
    elif a[0] in ["n", "N"]:                                              # if the first letter of the input is in the list (a list of strings which represents "n")
        active=False                                                      # it quits
    else :                                                                # if the input is not in the two lists, it is inconclusive and it starts asking questions
        active=True
    return active

#---------------------------------------------------------------------------------




