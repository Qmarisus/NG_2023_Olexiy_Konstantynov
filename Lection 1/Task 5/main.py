print("Дано рівняння виду ax^2+bx+c=0. Введіть значення a,b,c.")
a=int(input ("a = "))
b=int(input ("b = "))
c=int(input ("c = "))
d= pow(b,2)-(4*a*c)
if(d>0):
    x1=(-b-pow(d,0.5))/(2*a),
    x2=(-b+pow(d,0.5))/(2*a),
    print("Корені рівняння: x1=",x1,"\n", "x2=",x2)
elif(d==0):
    x=-b/(2*a),
    print("Рівняння має єдиний корінь. Х=",x)
else:
    x1= (-b-pow(abs(d),0.5)*1j)/(2*a),
    x2= (-b+pow(abs(d),0.5)*1j)/(2*a),
    print("Розв'язки рівняння: x1=",x1,"\n", "x2=",x2)

    