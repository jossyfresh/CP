# Get number of lines
l : int = int(input())
# Initialize ans
ans : int = 0    
# Initialize temp
temp : list = []
# Loop over each line
for t in range(l):
    # Get line and split into list
    x : list = input()
    x : list = x.split(" ")
    # Check if first word is add
    if x[0] == "add":
        # Call add function
        ans : int = add(ans, temp)
    # Check if first word is for
    elif x[0] == "for":
        # Push int onto temp
        temp : list = temp.append(int(x[1]))
    # Check if first word is end
    elif x[0] == "end":
        # Pop int off of temp
        temp : list = temp.pop()
# Check if ans is greater than 2^32 - 1
if ans : int > (2**32)-1:
    # Print overflow
    print("OVERFLOW!!!")
else:
    # Print ans
    print 1