
limit=input().split()                          # splitting the two intergers: fire safety limit and no of events

denied_groups=[]                               # a list for denied groups
party=0                                        # starting the party with 0

for i in range(int(limit[1])):                 # limit[1] is no of events
  event = input().split()                      # as input is string and a integer, event[0]="enter" or "leave"
  if 0<=party<=int(limit[0]):                  # limit[0] is fire safety limit
    if event[0]=="enter":                      # checking for enter or leave, event[1]=no of people(count)
      if party+int(event[1])<=int(limit[0]):   # adding given no of people to the people in the party and checking with the limit
        party+=int(event[1])                   # letting to the party if possible
      else:
        denied_groups.append(int(event[1]))    # if not possible adding the group to the list
    else:
      party -= int(event[1])                   # subtractig the no of people in the party
                                               #if the input is not "enter" (it would be leave)
print(len(denied_groups))                      # no of denied groups

