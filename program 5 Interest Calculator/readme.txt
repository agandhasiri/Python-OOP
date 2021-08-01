---------------------------------------
Authors: akhil.gandhasiri@slu.edu


---------------------------------------
Approximate number of hours spent: 

3 hrs 


---------------------------------------
Citation of any help received from (approved) sources:

None

---------------------------------------
Brief overview of program, including any known bugs:

for the greeeting function i have given the whole greeting message in a print function and assigned it as greet.
When you call greeting function,it returns the greet.

for the getRate function, open a while loop as True. In the loop there are two lists, one for the tuples which has
choices with alphabetic order. And other list for all the numbered alphabets. for the alphabetic numbering, there is a for loop
with enumerating choices. Used chr() method for the alphabetic numbering. After adding all to the lists, ask for the input.
if not in the list, it gives amessage and asks again for the valid input. if it is in the alphabests list, a for loop is
used to check the alphabet in the tuple list. when it finds the given input in the tuples, take the value from that tuple
and convert to desired value and store. Then turn loop as False and the while loop stops. After the loop it returns the stored
desired value.

for the getPrincipal function, assign the input to 0 and open a while loop as True. First there is an error checking, if the input is
less than 1 and not in between 1 and the limit, it gives a message and asks for the input again. When there is a valid input,
split the input into two, value before decimal point as one and value after decimal point as one. Then if the length of the value
which is after the decimal point is greater than three, it gives a message and asks for the value input again. when there is a
valid input, it stores the value and returns it with two decimal points.

for the computeBalance function, convert the principal into float and  there is a formula for computing the balance. It returns
the balance value.

for the display table, used f string to print all the things as desired, values with the adjustment and required decimal point.

for askYesNo, there is a list with all the strings that represents or equal to "yes". if the input is in the list, active will still be
True and the computation start again. if the input is not in the list, it quits.


---------------------------------------
Other comments or response program-specific questions:

I am confused with the askYesNo function that if the input is different from expected, should it start asking questions and compute
again or it has to quit.


