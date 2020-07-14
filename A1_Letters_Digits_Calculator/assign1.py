#Alaa' Omar
string=input("Please, enter your string:")
digits=0
letters=0
for i in string:
      if(i.isdigit()):
            digits=digits+1
      letters=letters+1
print(f"The number of digits is: {digits}")
print(f"The number of letters is: {letters}")
