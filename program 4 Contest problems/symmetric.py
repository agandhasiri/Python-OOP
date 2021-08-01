all_lists=[]                          # a list for all the arranged lists

while True:                           # a loop for every set

  n=int(input())                      # no of strings

  if n==0:
    break

  list=[]                             # a list for the given names
  for i in range(n):                  # accepting the no of strings equal to n
    name=input()                      # names
    list.append(name)                 # add every name to the list


  list1=list[0: :2]                   # adding names form original list with a step starting from first name
  list2=list[1: :2]                   # adding names form original list with a step starting from second name
  arranged_list=list1 + list2[ ::-1]  # actual list with expected results (arranged names)
  all_lists.append(arranged_list)     # adding every list to a new list



for j in range(len(all_lists)):       # taking all the lists
  print("SET"+" "+ str(j+1))          # print set no
  for v in range(len(all_lists[j])):  # print every name from the arranged list
    print(all_lists[j][v])
