uppercase_characters =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","K","R","S","T","U","V","W","X","Y","Z"]
lowercase_characters = ["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","k","r","s","t","u","v","w","x","y","z"]
symbols = ["!" ,"@", "#","%","$","&","*"]
numbers =['0', '1', '2','3', '4','5', '6','7','8','9']
print(uppercase_characters)
print(lowercase_characters)
print(symbols)
print(numbers)
user_input_minlength = "value"
user_input_maxlength = "value"
password_length =''
def password_generator() :
    user_input_minlength = int(input("enter the minimum length of the password"))
    user_input_maxlength = int(input("enter the maximum length of the password"))
    password_length = (user_input_maxlength + user_input_minlength)/ 2
    print(password_length)
while password_length != 0 :
     password_generator()
     uppercase_characters= input("pick upper case characters from list")
     lowercase_characters = input("pick lower case characters from list")
     symbols =input("pick a symbol")
     numbers = input("pick numbers")
     password_1 = uppercase_characters + lowercase_characters + symbols + numbers 
     password_2 = lowercase_characters + uppercase_characters + numbers  + symbols                                                                                                                                                                                 
     password_3 = numbers + uppercase_characters + symbols + lowercase_characters
     password_4 = symbols +  lowercase_characters + numbers + uppercase_characters
     print(password_1)
     print(password_2)
     print(password_3)
     print(password_4)