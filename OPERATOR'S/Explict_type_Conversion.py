# Explict type Conversion or cast Type conversion
# User have the right to convert one Data_type to another Data_type conversion

# Example 1
a=5
b=2
value=a/b
print(type(value))
int_value=int(value)
print(int_value)
print(type(int_value))

# Example 2

q=20
u=10
r=q+u
print(r)
print(type(r))

# Example 3
#q=20
#u="10"
#print(type(u))
#r=q+u
#print(r)
#print(type(r))

# Example 4
q=20
u="10"
r=q+int(u)
print(r)
print(type(r))

# Example 4
#q=20
#u="Nitish"
#r=q+int(u)
#print(r)
#print(type(r))

# Float to integer

n=10.36
r=int(n)
print(r)
print(type(r))

#Integer to float

m=10
l=float(m)
print(l)
print(type(l))

#Integer to complex

e=10
y=complex(e)
print(y)
print(type(y))

#Integer to String

k=10
o=float(k)
print(o)
print(type(o))

#String to Tuple

n="NitishMahato"
u=tuple(n)
print(u)
print(type(u))

#String to List

n="NitishMahato"
u=list(n)
print(u)
print(type(u))

#list to String

n=("Nitish","Mahato")
u=list(n)
print(u)
print(type(u))
#list to tuple

n=("Nitish","Mahato")
u=tuple(n)
print(u)
print(type(u))

a=10
result=bin(a)
print(result)









