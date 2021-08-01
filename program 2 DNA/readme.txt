---------------------------------------
Authors: akhil.gandhasiri@slu.edu

For projects that allow collaboration, ONE partner should submit
all materials, making sure both partners are identified above.
If a single author, provide a single email address.

---------------------------------------
Approximate number of hours spent: 
4
---------------------------------------
Citation of any help received from (approved) sources:
No
---------------------------------------
Brief overview of program, including any known bugs:
    
First step is to ask the input (DNA sequence and Pattern).
In the code i reversed the given pattern and then found the starting index places
of the pattern and reversed pattern in the given DNA. Then used these indexes for slicing the DNA with the
length of the pattern. Then found the middle and reversed it using( [::-1] ). Prefix and suffix can be known
by using index. At last i have added the strings as per the given rules. we can add all these in the way we want.

for the sequences like  joint pattern and reversed pattern i have written the code like
DNA.find(reverse_pattern,a+c), a is index of pattern and c is length of the pattern,
so that it checks the reversed pattern after the occurance of complete pattern.

---------------------------------------
Other comments or response program-specific questions:

my code may not be the best, but i have written it for clear understanding.
---------------------------------------
