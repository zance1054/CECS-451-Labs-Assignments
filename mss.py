# Alexander Fielding
# assn0
# max sub array example

def mssl(alist):
    best = 0
    curr = 0

    for i in alist:
        curr = max(curr + i,0)
        best = max(best,curr)

    return best


#Main

alist = []
quit = ""

while(quit!= "q"):
    q = input("Enter q to to quit, or a number to add to the array" + "\n")

    if q == "q":
        break;
    else:
        alist.append(int(q))

answer = mssl(alist)

print(answer)
