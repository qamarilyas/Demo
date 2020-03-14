str='aB2'

print(any(i.isalnum()  for i in str))
print(any(i.isalpha()  for i in str))
print(any(i.isdecimal() for i in str))
print(any(i.islower() for i in str))
print(any(i.upper() for i in str))
