Tests = int(input())                # no of test cases
len_list=[]                         # for length of each test case list with distinct names
for v in range(Tests):              # a loop for every test case
    n = int(input())                # no of work trips for each test case
    list = []                       # a list for distinct names
    i=0
    while True:
        name = input()              # name of the place
        if name not in list:        # checking for the name in the list
            list.append(name)       # adding that name to the list, if it is not in the list.
        i+=1                        # counting every trip
        if n==i:                    # if the count is equal to n(no of trips)
            break                   # it stops taking trip name
    len_list.append(len(list))      # add length of every test case list to a new list
for j in len_list:                  # print length of every distinct names list
    print(j)


