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

match math_operation:
    case '+': 
        result=plus(a,b)
    case '-':
        result=min(a,b)  
    case '*':
        result=mult(a,b)   
    case '/':
        result=div(a,b)
    case 'pow':
        result=pow(a,b)    
    case 'root':
        result=root(a,b)  
    case _:
        print('Ви допустили помилку при введенні, перезапустіть програму i повторіть ще раз'),
        exit()
    
print ('Результатом математичноъ операції є число: ', result)     



