# Introduction:
TITLE="\n\nWelcome to the PYTHON CALCULATOR"
print(TITLE,"\nCreated by: Aaryan Kumar")

# Decision:
decision=input("\nDo you want to open calculator, Enter [yes/no]: ")

# Calculator algorithm:
while decision=="yes":
    # Two number input by User:
    Num1=int(input("Enter your FIRST NUMBER: "))
    Num2=int(input("Enter your SECOND NUMBER: "))
    # Operation Input by User:
    operation='''$~~~LIST OF OPERATION~~~$
    1. For Addition type "+"
    2. For Substraction type "-"
    3. For Multiplication type "*"
    4. For Division type "/"'''
    print(operation)
    op=input("Enter your operation : ")
    # Performing operation Algorithm
    match op:
        case '+':
            print(Num1,"+",Num2,"=",Num1+Num2)
        case '-':
            print(Num1,"-",Num2,"=",Num1-Num2)
        case '*':
            print(Num1,"*",Num2,"=",Num1*Num2)
        case '/':
            print(Num1,"/",Num2,"=",Num1/Num2)
        case _:
            print("invalid operation")
    decision=input("Do you want to open Calculator again:")  
else:
    print("\nOK...!\nSee you next time...!")      
      