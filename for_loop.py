#Let's use the variable num in the for loop to determine which list number should print.
dataset1 = {0, 1, 2, 3, 4}
datalist1 = [89, 72, 0, 96, 98]
for num in dataset1:
    print(num)
    print(datalist1[num])
    
    
#Let's now stick an if statement in there to only print A or higher scores.

for num in dataset1:
    if datalist1[num] > 90:
        print(str(num + 1) + "th score is an A: " + str(datalist1[num]))

