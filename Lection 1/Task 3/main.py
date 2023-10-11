temp_scale = (input('Choose whether you want to convert to Celsius(c) or Fahrenheit(f)'))
temp = (float(input('Enter the temperature value you want to convert: ')))
if(temp_scale=='c'):
    temp = (temp-32)/1.8
    print('Converted value = ', temp)   
elif(temp_scale=='f'):
    temp = (temp*1.8)+32
    print('Converted value = ', temp)   
else:
    print ('Error! You entered incorrect number!')
 
         
    