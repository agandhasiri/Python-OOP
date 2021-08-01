DNA=input("Enter a DNA sequence: ")
pattern=input("Enter the pattern: ")

reversed_pattern=pattern[::-1]
a=DNA.find(pattern)                                                    # Finding start index of pattern
c=len(pattern)                                                         # Finding length of pattern
b=DNA.find(reversed_pattern,a+c)                                       # Finding start index of reversed pattern after complete pattern
middle=DNA[a+c:b]                                                      # Finding Middle
reversed_middle=middle[::-1]                                           # Reversing middle
mutated_dna=DNA[:a]+pattern+reversed_middle+reversed_pattern+DNA[b+c:]
                                                                       # Adding prefix,pattern,reversed middle,reversed pattern,suffix
                                                                       # pattern can be added to the prefix as a+c
print("Prefix:",DNA[:a])                                               # prefix is from 0 to start index of pattern
print("Marker:",pattern)
print("Middle:",middle )
print("Reversed Middle:",reversed_middle)
print("Reversed Marker:",reversed_pattern)
print("Suffix:",DNA[b+c:])                                             # suffix is from reversed (pattern + pattern length)till end 
print("Result:",mutated_dna)
