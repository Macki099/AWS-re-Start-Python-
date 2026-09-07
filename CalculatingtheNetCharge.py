# Python3.11  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

#To match the code segment, add the following key-value pairs into the dictionary.
#'c': 8.18
#'k': 10.53
#'h': 6.00
#'r': 12.48
#'d': 3.65
#'e': 4.25
#The dictionary should look like the following code:

pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

#To identify a count of an item within a list, you can use the count() method. To see how many amino acids in insulin are Y, use the count() method by entering: insulin.count("Y")
#Next, update the insulin.count() line by casting the variable returned by the count() method as a float: float(insulin.count("Y"))
#Now that you have the basis for identifying a single entity, you can use this method to find all entities from a list. This process can be done by using list comprehension. For the entire line, enter:

seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# Writing the net charge formula
#Create a variable called pH and initialize it to zero by entering pH = 0 and pressing ENTER.
#Create the while loop by entering while (pH <= 14): and pressing ENTER.
#Copy the following netCharge variable and paste it at the beginning of the while loop.
pH = 0

while pH <= 14:
    netCharge = (
        +(sum({
            x: ((seqCount[x] * (10 ** pKR[x])) /
                ((10 ** pH) + (10 ** pKR[x])))
            for x in ['k', 'h', 'r']
        }.values()))
        -
        (sum({
            x: ((seqCount[x] * (10 ** pH)) /
                ((10 ** pH) + (10 ** pKR[x])))
            for x in ['y', 'c', 'd', 'e']
        }.values()))
    )

#To print the netCharge variable with the pH, use a format string for better readability. Enter print('{0:.2f}'.format(pH), netCharge) and press ENTER.
#Finally, increment the pH variable by entering pH +=1 and pressing ENTER.
#Save and run the file.

    print('{0:.2f}'.format(pH), netCharge)
    pH += 1



