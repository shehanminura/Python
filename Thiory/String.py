name = "shehan"
print(len(name)) #6
age=45
#print(len(age))     'int' has no len()
age="45"
print(len(age))  #2
print(type(age))  #<class 'str'>
print(age.isdigit())  #number da yanna balayi   #True
print(name.isdigit())    #False
marke=90
#print(marke.isdigit())  AttributeError: 'int' object has no attribute 'isdigit'
print(name.isalpha())  #letter da yanna balayi  #True
print(age.isalpha())
email = "shehan@gmail.com"
print(email.isalpha())
print(email.isalnum())

temperature = "-2"
print(temperature.isdigit())  #false
print(temperature.isalnum()) #False
password = 'shehan123'
print(password.isalnum()) #ilakkam ha akuru

name="shehan123"
print(name.isalpha())
print(not password.isalpha())
print(email.isalnum())
print(temperature.isalnum())


print(age.isalnum())
print(name.isalnum())
print(password.isalnum())


name="shehan"
print(name.capitalize())   #first latter capital    Shehan
print(name.swapcase())     #SHEHAN   kapital & simpal maru kirima sidu karyi
print(name.lower())    #shehan
print(name.upper())    #SHEHAN
print(name)  #shehan
name = name.capitalize()
print(name.swapcase())
