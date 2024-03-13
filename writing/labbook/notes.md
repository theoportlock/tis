# docs
remake figure for input memory action plan
complete project aims in publication docs
continue work on background

# recuitment
for portlock lab - work on google collab maybe?
need to delegate tasks, best way to be productive

# tis
Work out sparcity - fix the bitarrstats
Make book/guide of figures for tis
Actions like dna transcription
activating things its connected to - work out how to do the "slice memory array with input array for action"
Sort comb by pairs etc
need to focus on finding similar patterns to those observed and working out predictions of missing data (maybe not even missing and just comparing what you see to what you predict - binning memories)
focus on more basic experiments (bit adding etc)
figure out how to change slice of combination search during search
make intracombination priority list for active bit checking
change all functions to yield

# experiments
NEED A FLOWCHART OF EXPERIMENTS
List of checkpoints that the software must acheive before progression
parrot
    Desc: simple repetition of input using translation through I/O
    Goal: quick repitition measured using accuracy (correct/all)
memory
    Desc: learn pattern recognition of an internal sequence
	Goal: predict the d in abcd abxd
addition
	Desc: calculate sum of two positive integers
    Goal: correct more often than not
competition
    Desc: find two scores, delete failure and replicate victor 
    Goal: ?
turing
    Desc: generic turing test with a conversation
    Goal: a consensus of people believe that it is also a person?
sinepredict
    Desc: input is the sin(previous input)
    Goal: predict the next number
final
    Desc: replace human decision making
    Goal: metrics of human wellbeing

# ideas
Simultaneous equations
DATASETS FROM openml https://www.openml.org/search?type=data&sort=runs&status=active&id=31
Need some way of having continuous running and monitoring dashboard

# TODO
Start with understanding the schematic
Need whiteboard and network plotting to create plan
Input nodes the same as output in structure?
Only do/recreate whats seen before - random differences can change the output (mutation) - if those  differences increase the chance of survival then there is a higher probablity that that action will be seen

# Steps
## Input
Important to have a way of dealing with time
	this could be using a plus one matrix
		could reduce the number of possible combinations by slicing here
		on memory also?
	could do this using delay
		could be on the memory also

## Memory
Also could be called combinations
Important to look at relative combinations (multiply for scaling and addition for sliding)
time independant?
Probablistic or combinatoric

## Output
Also could be called action
Two activation components - Random and Nonrandom
Random activation from combination of memory
	in addition to the random action without?
	How to manipulate/decide permenance of random action?
Same time conciderations of input

# Process
Random output -> input are memorised
    In this step the consequences of actions are remembered
    can only see with the correct teporal resolution
        temporal resolution is adjusted with A1A1 memories
 
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

# READING
Why value philosophy?
"The value of philosophy is, in fact, to be sought largely in its very uncertainty. The man who has no tincture of philosophy goes through life imprisoned in the prejudices derived from common sense, from the habitual beliefs of his age or his nation, and from convictions which have grown up in his mind without the co-operation or consent of his deliberate reason. To such a man the world tends to become definite, finite, obvious; common objects rouse no questions, and unfamiliar possibilities are contemptuously rejected. As soon as we begin to philosophize, on the contrary, we find that even the most everyday things lead to problems to which only very incomplete answers can be given."
— Bertrand Russell, The Problems of Philosophy (1912), Ch. XV: The Value of Philosophy, p. 141

# Application of Upgrade framework - create scenario to test
NOTATION XI/OY , X = node, Y = time
Attempt to denoise the world

SCENARIO ONE
Andy is in a mathematics class. The teacher asks him: 'what is 1+1?' . [ 1i1 ]
Andy answers the question correctly by chance: '2' . [ 1i1 + 1o2 ]
The teacher achnowledges the correct answer: 'Correct' . [ 1i1 + 1o2 + 2i3 ] 
- Somebody has to answer correctly for the determination of correctness to be made (2i3)

SCENARIO ONE REDO
Andy's friend Ben answers correctly 
- There needs to be recognition that Ben's actions can be replicated by Andy

SCENARIO ONE REDO REDO
Andy's friend Ben says the word '2' . [ i4 ]
Ben says the same word by chance: '2' . [ o1 + i4 ]

SCENARIO ONE REDO REDO REDO
Ben says the word '2'
Ben recognises the input: '2'
Andy's friend Ben says the word '2'
Ben recognises the same word '2'
The teacher asks Ben: 'what is 1+1?'
Ben answers the question correctly by chance: '2'
The teacher achnowledges the correct answer: 'Correct'

SCENARIO ONE REDO REDO REDO REDO
Ben says the word '2'
Andy recognises the input: '2'
Andy says the word '2'
Andy recognises the connection between what he says and what Ben says
The teacher asks Ben: 'what is 1+1?'
Ben answers the question correctly: '2'
The teacher achnowledges the correct answer: 'Correct'
Andy recognises the connection between ben's '2' (and '2' in general) and the teachers 'Correct' subsequently

# Can work without but Issues to solve
Zoom and stretch
Explosion


# need a new test - determinism
