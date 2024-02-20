def country():
    print("I am a Kenyan.")

country()

def calculator(num1, num2, operator):
    
    if operator == '+':
        result = num1 + num2
        return result
    
    elif operator == '-':
        result = num1 - num2
        return result

    elif operator == '*':
        result = num1 * num2
        return result

    elif operator == '/':
        result = num1/num2
        return result
    
print(calculator(4,5,'+'))
print(calculator(7,4,'-'))
print(calculator(100,50,'*'))
print(calculator(36, 6, '/')
      )