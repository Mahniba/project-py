#BMI calculator in python
result = "value"
def BMI():
    VALUE1 = float(input("enter the value of height:"))
    VALUE2 = int(input("enter the value of the weight:"))
    result =VALUE2 / ((VALUE1)*(VALUE1))
    print(result)
def choices():
     print("your choices are:")
     print("a.1-10")
     print("b.11-25")
     print("c.26-90")
     print("d.91-120")
while result != 0:
       BMI()
       choices()
       key = input("enter your choice:")
       if key == "a.1-10":
         if "result <= 20":
          print("very healthy")
       elif key == "b.11-25" :
         if "result<= 32":
          print("that's good")
       elif key == "c.26-90" :
         if "result<= 34":
          print("sweet")
       elif key == "d.91-120" :
          print(result)


