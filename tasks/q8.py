
def add(i,j):
    return int(i) + int(j)
def multiply(i, j): 
    return int(i) * int(j)
def divide(i, j):
    if j != 0:
        return float(i) / float(j)
    else:
        return "Cannot divide by zero."
def subtraction(i, j):
    return int(i) - int(j)
def main():
    a=input(print("please enter first number"))
    b=input(print("please enter second number"))
    choice=input(print('''please select the operator in term of number
        1: for addition
        2: for multiplication
        3: for division 
        4: for subtraction '''))
    if choice == '1':
            result = add( a, b )
    elif choice == '2':
            result = multiply(a, b)
    elif choice == '3':
            result = divide(a, b)
    elif choice == '4':
            result = subtraction(a, b)
    else:
         print("INVALID CHOICE MADE.")
    print(f"Result: {result}\n")

if __name__ == "__main__":
    main()

    
