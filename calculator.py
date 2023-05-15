def add():
      a=float(input("enter the first digit"))
      b=float(input("enter the second digit"))
      sum=a+b
      return sum
def subtract():
    a=float(input("input the first digit"))
    b=float(input("enter the second digit"))
    difference=a-b
    return difference
def multiply():
     a=float(input("enter the first digit"))
     b=float(input("enter the second digit"))
     product=a*b
     return product
def divide():
      a=float(input("enter the first digit"))
      b=float(input("enter the second digit"))
      division=a/b
      return division

while True:
     options=input("1.Add\n 2.Subtract\n 3.Multiply\n 4.Divide\n 5.Exit\n")
     if options=='1':
        print(add())
     elif options=='2':
        print(subtract())
     elif options=='3':
        print(multiply())
     elif  options=='4':
         print(divide())
     elif options=='5':
         break
     else:
         print("enter valid options")
         
    

    
