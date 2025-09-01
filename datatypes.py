age = 12
name = 'Vihaan'
surname = "Chanda"
country = 'India'
weight = 57.1 #kg
isStudent = True

print(f"My name is {name} I am {age} years old. I am from {country} and I weigh {weight} ")
print(type(age))
print(type(name))
print(type(country))
print(type(weight))
print(type(isStudent))

weight = int(weight)
print(weight)
print(type(weight))

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))


print("Addition :", num1+num2)
print("Difference :", num1-num2)
print("Product :", num1*num2)
print("Division :", num1/num2)
print("Floor Division:", num1//num2)
print("Remainder :", num1%num2)
print("Exponent :", num2**2 )
print("Square Root :", num1**0.5)

myName = (name+" "+surname)
print(myName)
initial = (myName[0]+"."+myName[7])
print(initial)

