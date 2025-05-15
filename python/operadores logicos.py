"and"
num1=5 
num2=5
num3=10
print(num1==num2 and num1!=num3) #False
print(num1==num2 and num1>num3) #False
print(num1!=num2 and num1>num3) #False
print(num1!=num2 and num1<num3) #True
"or"
print(num1==num2 or num1!=num3) #True
print(num1==num2 or num1>num3) #False
print(num1!=num2 or num1>num3) #False
print(num1!=num2 or num1<num3) #True
"not"
print(not(num1==num2))  #False              
print(not(num1!=num2))  #True
print(not(num1>num3))   #True
print(not(num1<num3))   #False
