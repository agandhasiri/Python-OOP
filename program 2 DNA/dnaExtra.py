DNA=input("Enter a DNA sequence: ")
pattern=input("Enter the pattern: ")

reversed_pattern=pattern[::-1] 
split1=DNA.split(pattern,1)
split2=split1[1].split(reversed_pattern,1)
c=split2[0]

print("Prefix:",split1[0])                                               
print("Marker:",pattern)
print("Middle:",c)
print("Reversed Middle:",c[::-1])
print("Reversed Marker:",reversed_pattern)
print("Suffix:",split2[1])                                             
print("Result:",split1[0]+pattern+c[::-1]+reversed_pattern+split2[1])
