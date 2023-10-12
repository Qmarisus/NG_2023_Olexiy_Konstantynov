user_list = []
while True:
    user_input=input("Enter the element or 'end' for completion of input.")
    if user_input!='end':
        user_list.append(user_input)
    else:
        break
without_clones=[]
for element in user_list:
    if element not in without_clones:
        without_clones.append(element)
print ("The elements of the list:", without_clones)