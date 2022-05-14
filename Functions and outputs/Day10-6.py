def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}



num1 = int(input("what's the first number?:"))
num2 = int(input("what's the second number?:"))

for symbol in operations:
    print(symbol)
Operation_symbol=input("Pick an operation from above line:")

cal_function=operations[Operation_symbol]
answer=cal_function(num1,num2)

print(f"{num1} {Operation_symbol} {num2}={answer}")



