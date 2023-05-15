#to-do list in python
user_input ="random"
#using dictionary as storage
store = {}
print(type(store))
def request():
    print("your choices are:")
    print("i.add")
    print("ii. view")
    print("iii. delete")
    print("iv. exit")
while user_input != "exit" :
    request()
    user_input=input("enter your choices:")
    if user_input =="add" :
        key = input("what number do you want ")
        item = input("what do you want to add here")
        store.update({key:item})
        print("first item added!", item)
    elif user_input == "delete" :
        key = input("what do you want to delete")
        item = input("what do you want to delete")
        if key and item in store:
            store.pop(key,item)    
            print("deleted item:", item)
        else:
            print(" item doesn't exist in the list")
    elif user_input == "view":
        print("list of things to do")
        print(store)
    elif user_input == "exit" :
        print("next time")


