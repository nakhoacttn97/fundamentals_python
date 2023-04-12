"""
@author: KTPHUONG
@version: 1.0
@since: Jan 05, 2017
"""

"""
count = 1
while count <= 5:
    print (count, " <= 5")
    count += 1
else:
    print (count, " > 5")
    
for num in range(10,20):  #to iterate between 10 to 20
    for i in range(2,num): #to iterate on the factors of the number
        if num%i == 0:      #to determine the first factor
            j=num/i          #to calculate the second factor
            print ('%d equals %d * %d' % (num,i,j))
            break #to move to the next number, the #first FOR
    else:                  # else part of the loop
        print (num, 'is a prime number')

for item in range(1,11):
    if item %2 != 0:
        print('item ', item ) 
else:
    print ('Finish loop!')



for letter in 'Phuong':     
    if letter == 'o':
        continue
    print ('Current Letter :', letter)

var = 10                   
while var > 0:     
    if var == 6:
        continue    
    if var %2 == 0:              
        print ('var :', var)
    var -= 1   

for letter in 'Phuong': 
    if letter == 'o':
        pass
        print('Pass block')
    print('Current Letter :', letter)

print('Out of for!')    

print('Hello') 
print("Hello") 
"""
# Function definition is here
def printme(str):
    # This prints a passed string into this function
    print(str)
    return;

# Now you can call printme function
printme('Hello & welcome Python')

