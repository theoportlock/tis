# TODO
Start with understanding the schematic
Need whiteboard and network plotting to create plan
Input nodes the same as output in structure?
Only do/recreate whats seen before - random differences can change the output (mutation) - if those  differences increase the chance of survival then there is a higher probablity that that action will be seen
Three sources of learning, I/I, I/O, and O/O
combination nodes to check accuracy of prediction guess
flow be made to be parallelized? (don't need to do all neurons, just flow of information)

# Input
Important to have a way of dealing with time
	this could be using a plus one matrix
		could reduce the number of possible combinations by slicing here
		on memory also?
	thous could be using delay
		could be on the memory also

# Memory
Also could be called combinations
Important to look at relative combinations (multiply for scaling and addition for sliding)
time independant?
Probablistic or combinatoric
A decay function for persistent node activation (different per node?)
Excitatory vs inhibitory neruons (can't be both)
neurons that fire together wire together (hebbian) - opposite is true (synaptic pruning)

# Output
Also could be called action
Two activation components - Random and Nonrandom
Random activation from combination of memory
	in addition to the random action without?
	How to manipulate/decide permenance of random action?
Same time conciderations of input

# Properties of a node
decay function
inactivation time after activation
has a set of output and input edges (save both?)
prime number indexing?

# Process
1. random output -> input are memorised (I/O)
1. input combinations are memorised (I/I)
1. work on predicting the inputs using output and memory

# Performance metric
Need a way to visualise and measure the success of all components
	Sum of matrix
	beta distribution between memory arrays
	alpha diversity also

# Testing
Need a continuous source of input and output
Stocks
robotics

# Recruitment
Selling the three node model

# Deadlines

