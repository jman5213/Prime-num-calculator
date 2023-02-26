# Prime-num-calculator

### How it should work

#### First:

Get the User's input for the nth prime number to return

#### Second:

Initiate the variables needed to run the code

| Variable Name | Variable Function                          |
|---------------|--------------------------------------------|
| currentPrime  | the last calculated prime number           |
| calcThru      | the user's input                           |
| currentNum    | the program checks if this number is prime |

#### Third:

if the current number is not even:
  loop through a list of numbers that starts at three and ends at 
  (current number + 1)/2, and skips every even number, where i is 
  the current item of the list
  
  I do this because the number at most will be divisible by half of itself, but since the number is odd, you must add or subtract 1 in order to return an even number. I also skip every even number because an odd number will never be divisible by an even number.
  
  In the for loop, I use the modulo (%) to see if the current number is divisible by the current item of the list. If the returned value is 0 (there is no remaider), then I increase the current number by 2 (to skip even numbers), and print "breaking @ "+str(currentNum), then I 'break' out of the for loop.
  If I loop through the entire list, and none of the values are remainder 0, I print ("Didn't break @",str(currentNum),"divided by",i), and I make the last prime num found equal to the current number, then increase the current number by 2 (to skip even numbers).
  
#### Fourth:

I return the time take to finish the code (found with the time module's perf_counter() function) and print all of my variables with lables.

### Bugs:

The code goes into an infinite loop and doesn't incriment by 2 when it gets to the bottom of the for loop.
