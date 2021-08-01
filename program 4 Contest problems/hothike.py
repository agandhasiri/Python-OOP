n=int(input())                      # no of days
t=input().split()                   # temperature for each day with spaces
temps=[]                            # int values of temperatures
for i in t:                         # for loop to add values to list as int vaules
    temps.append(int(i))
m_v, max_temp = -1, 41              # assign max temp to 41 as the given max is 40
for v in range(n-2):                # a loop to check temperatures                                  # assign every time values of max temp
    m=max(temps[v], temps[v+2])     # check for max temp value for two hike days
    if m < max_temp:
        max_temp = m                # assign lesser value of temp as new max temp
        m_v = v                     # assign value of v
print(m_v+1 , max_temp)             # print start day, max temp

