# A program that reads the data from the text file.

# used a built-in function called open to read data  
f = open("DOB.txt", "r")

# created variables 
Names_of_people = [] 
D_O_B = []
n = 1 
N = 1

# used the for loop function,stip,split,append,and list   
for line in f:
    Line = line.strip ()
    Line = line.split ()
    Names_of_people.append(Line[0] +" " + Line[1])
    D_O_B.append(Line[2] + " " + Line[3] + " " + Line[4])

print("Names:")

# used for loop, string function  
for i in Names_of_people:
    print(str(n) +". " + i)
    n+=1 
  
print("\n Birth Date:")

# used a for loop, string fuction 
for i in D_O_B:
    print(str(N) + ". " + i)
    N+=1 

# used built in function to close program 
f.close()

# I was stuck rough way through the middle of my program so i did some research  
# https://www.bing.com/search?q=DOB+txt+python+pythonic+method+&qs=n&form=QBRE&sp=-1&pq=dob+txt+python+pythonic+method+&sc=0-31&sk=&cvid=EA3CD7B2018842C9B4DBDF4F8D9B0668&ghsh=0&ghacc=0&ghpl=&ntref=1#


