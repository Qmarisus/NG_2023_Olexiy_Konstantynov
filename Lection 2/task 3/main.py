num = int(input("Input your number: "))
table = []

p_num = []
for i in range(1, num+1):
    div = []
    for j in range(1, i+1):
        if i%j == 0:
            div.append(j)
    table.append((i, div))
    if len(div)==2:
        p_num.append(i) 
 
print ("Numbers and their divisions: ") 
for nums, divs in table:
    print(f"{nums}\t\t{' '.join(map(str, divs))}")      
    
print ("Primitive numbers: ", p_num)        





