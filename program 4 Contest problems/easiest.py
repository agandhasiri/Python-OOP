list=[]                            # achieved p value for every input
while True:
  N = int(input())                 # integer input
  
  if N==0:                         # it has to stop taking input when you give 0
    break

  v=sum(int(r) for r in str(N))    # sum of digits of the givrn no (N)


  p=11                             # p has to be more than 10
  while True:                      # loop until you get the result
    a=N*p                          # multiplying N with 11<p<answer

    s=sum(int(i) for i in str(a))  # sum of digits of (N*P)
      
    if v==s:                       # checking the two sums
      break                        # stopping if we achieve
    else:                          # else increase the value of p
      p+=1

  list.append(p)                   # add the answer(achieved p) to a list

for i in list:                     # print every value from the list
  print(i)


