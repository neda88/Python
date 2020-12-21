import random

UpperBound = 100
LowerBound = 1
number = random.randint(1, 100)
print("Choose a number between 1 and 100 in your mind: ")
print("I guessed" , number)
FeedBack = str(input("Please give me FeedBack : "))
count = 1
#while(FeedBack != 'C' and FeedBack != 'c'):   # This line is equivalent of the line below:
while(not(FeedBack == 'C' or FeedBack == 'c')):
    count += 1
    if (FeedBack != 'S' and FeedBack != 's'):
        LowerBound = number + 1
        #print (LowerBound, UpperBound)
        number = random.randint(LowerBound, UpperBound)
        print("I guessed" , number)
        FeedBack = str(input("Please give me FeedBack : "))
    elif (FeedBack != 'L' and FeedBack != 'l'):
        UpperBound= number - 1
        #print (LowerBound,UpperBound)
        number = random.randint(LowerBound, UpperBound)
        print("I guessed" , number)
        FeedBack = str(input("Please give me FeedBack : "))

print("Congradulations, you guessed it right in {} times".format(count) )
