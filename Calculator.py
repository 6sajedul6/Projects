def add (n1,n2):
    return n1+n2
def subtract (n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide (n1,n2):
    if n2==0:
        return "Its not possible"
    return n1/n2

operators={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    num1=float(input("Chose the 1st number:"))
    for key in operators:
        print(key)
    should_continue = True
    while should_continue:
        symbol = input("Chose your operator:")
        num2 = float(input("Chose the 2nd number:"))
        calculation= operators[symbol]
        first_answer=calculation(num1,num2)
        print(f"{num1} {symbol} {num2} = {first_answer}")
        if input(f"Type y to continue with {first_answer} or Type n to exit.")=="y":
            num1=first_answer
        else:
            should_continue=False
            calculator()


calculator()
