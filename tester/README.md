# Pattern Recognition

This is a project designed to find patterns in a bitarray datastream.

# Setup 

To begin, setup the python virtual environment with the following commands:
source tester/venv/bin/activate

deactivate afterward by:
deactivate

## 1. Pipeline Summary

1. Convert inputs into binary (inputs can be text or from file)
2. Measure distances between active nodes in the temporary array and output into a distances array
3. Find all combinations of active nodes in the distances array and output into combinations array. Each active combination element will represent a feature of the original input

## 2. Function Summary

1. addnewelement - Removes the rightmost element of an array, shuffles the information down towards that empty space and adds a new input node	
2. binadder - Removes the rightmost element of an array, shuffles the information down towards that empty space and adds a new input node
3. comb - returns a bitarray of all combinations of an input bitarray. Puts an incorrect empty bit at start of bitarray - to fix
4. splitter - returns bitarray of distances between active nodes in an array of total distance possibilities. This removes the effects of array transpositions and inversions
5. main - uses all above functions

## 3. Function Details

### 1. addnewelement
* Shifts the location of each data element of the first list (arg1) up by one
* Adds the second list (arg2) to the first element of the first list
* Returns the new list
This function should work fine for adding non equivalently sized arrays to one another.

### 2. binadder 
* Takes an input bitarray (arg1) and returns a bitarray that is 1+ the total binary value of the bitarray (reading from right (smallest) to left (biggest)) 
I understand that there are many more consise ways to write this formula and perhaps that an individual function is not necessary for this project. For now consiseness is not a matter of high importance to me, however if you want to suggest a quicker way to write this function then I will update.

### 3. combinations
* Inputs a single bitarray (arg1)
* For each possible binary number less than the total, if all 1's that are present in the search binary number are present in the input bitarray then append a 1 to an output array. If not then append a 0
* Returns the output bitarray
This function finds all combinations of 1's in an input bitarray. Works similar to nCr in maths

### 4. splitter
* Inputs a single bitarray (arg1) 
* For each possible distance between 1's in the bitarray, if that distance is observed then append a 1. If the distance between 1's is not observed then append a 0.
What this function effectively does is produce an array of 1D vectors of active nodes in the input bitarray. This way, even if the the bitarray is a datastream, the same distances are observed. Work still needs to be done here with regards to multidimensional inputs

### 5. main 
* Inputs a single bitarray
* Dripfeeds each element of that array into a new temporary array of a defined length
* After each dripfeed, the splitter function finds distances between 1's in the temporary array
* The combinations function is applied to the result of the splitter function to find the combinations of distances between 1's in the temporary array
* The position of each 1's in the results of this function is printed to the command line
This is the main file. By default, the input to this function is by a user prompt on the command line. However, using the inreader and outreader functions (5 & 6) can be used to read and write files respectively in the same directory as the running script. The length of the temporary array is a value that needs to be played around with depending on the sparcity of 1's in the original inputted bitarray. Changing the base of this inputted array would increase the sparcity of the input bitarray and is an action that's currently under investigation 

### 6. tester
inputs do not require an input

## 4. To do:

- Play around with node delay mechanics for pattern memory
- Create and link nodes that do an action when a pattern is recognised
- Real time reader and writer
- Investigate different inputs (jpg files e.t.c.)

I'm pretty new to all this, any suggestions more than welcome! 
