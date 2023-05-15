contact ={
    "name" : 000000000 
}
def contactbook():
  name=input("enter the name of the individual")
  number=int(input("enter the number of the individual"))
  contact[name] = number
  print(contact) 
while contact != 0:
    contactbook()
    continue