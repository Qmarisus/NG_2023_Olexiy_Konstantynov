def plus ( a, b):
    c=a+b
    return c

def min (a, b):
    c=a-b
    return c

def mult(a,b):
    c=a/b
    return c

def div(a,b):
    c=a/b
    return c

def pow(a,b):
    c=a**b
    return c

def root (a,b):
    c=a**(1/b)
    return c
  
math_operation = (input("Виберіть математичну дію +,-,/,*,pow,root: "))
a=(float(input("Введіть перше число: ")))
b=(float(input("Введіть друге число: ")))

if (math_operation=='+'):
    result=plus(a,b)
elif(math_operation=='-'):
    result=min(a,b)
elif(math_operation=='*'):
    result=mult(a,b)
elif(math_operation=='/'):
    result=div(a,b)
elif(math_operation=='pow'):
    result=pow(a,b)
elif(math_operation=='root'):
    result=root(a,b)
else:
    print('Ви допустили помилку при введенні, перезапустіть програму i повторіть ще раз'),
    exit()

print('Результатом математичноъ операції є число: ', result)    


