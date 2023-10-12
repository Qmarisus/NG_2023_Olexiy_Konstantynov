user_list=[]
 
while True:
    user_input=input("Input elements of list. Type 'end' for completion of input.")
    if user_input!='end':
        try:
            nmbr=float(user_input)
            user_list.append(nmbr)
        except:
            user_list.append(user_input)
        
    else:
        break
    
num_list=[]
for num in user_list:
    if isinstance(num, (int, float)):
        num_list.append(num)
    
print ("Elements of the list:", num_list)   
print ("Number of numbers in the list:", len(num_list))     