'''
Operators
------------
Operators indicates what operation is to be perfomed.

Operands
----------
Operands indicates on what the action or the operation should be performed.

Types of Operators
----------------------
Operators can be further divided into 6 categories:
    1. Arithmetic Operators
    2. Comparision Operators
    3. Logical Operators
    4. Assignment Operators
    5. Identity Operators
    6. Membership Operators
    7. Bitwise Opertors


1. Arithmetic Operators
-----------------------------
    Addition, Subtraction, Multiplication
    Floor division, Exponentiation,
    Division, Modulus
'''

#Exponentiation
print(8**2)

#Modulus
print(8%3)

#Floor Division
print(5//2)


'''
2. Comparision Operator
    <   less than
    <=  less than or equal to
    !=  not equal to
    ==  equal to
    >=  greater than equal to
    >   greater than
'''

print("----------------")
print("Greater than or equal to")
print(3>2)
print(5>=9)
print("----------------")
print("Equal to or not equal to")
print(3==3)
print(3==4)
print(3!=3)
print(3!=4)
print("-----------------")
print("less than or equal to")
print(3<2)
print(5<=9)
print("-----------------")


print("Logical Operator")
'''
3. Logical Operators
    1. and (True---Both should be true)
    2. Or  (True---any one should be true)
    3. not (True---if false)
'''
print("And-------")
print(3>2 and 3>7)
print(3>2 and 9>7)
print("or--------")
print(3<2 or 3>7)
print(3>2 or 9>7)
print("not---------")
print( not 3>4)
print( not 3<4)


'''
4. Assignment Operators
    --used in Python to assign value to variables
    
    Types of Asignment Operator
        1. =
        2. +=
        3. -=
        4. *=
'''

print("------------------------")
a=5

b=a
print(b)
b+=2
print(b)
b-=2
print(b)
b*=5
print(b)
b/=2
print(b)


'''
4. Identity Operators
    Identity operators are used to compare items to see if they are the same object with the same memory address
    
    Types:
        1. Is
        2. Is not
'''
a=1234
b="1234"
print('-----------------')
print(a is b)
print(a is not b)

print("-----------------")
b=1234
print(a is b)
print(a is not b)

'''
Bitwise Operators
    These Operators are used to compare the Binary numbers
    
    Types:
        1. AND(&) Operator
            0&0=0
            0&1=0
            1&0=0
            1&1=1
            
        2. OR(|) Operator
            0|0=0
            0|1=1
            1|0=1
            1|1=1
            
        3. XOR(^) Operator
            0^0=0
            0^1=1
            1^0=1
            1^1=0
            
        4. << zero fill left shift
            5<<2=10
            6<<2=3
            
        5. >> zero fill right shift
'''
print("Bitwise Operator")
print(8&10)
print(8|10)
print(8^10)

print(5<<1)
print(5<<2)

print(5>>1)
print(5>>2)


'''
Membership Operator
Membership operators are used to check the presence of a sequence in an object.
Types:
    in
    not in
    
'''
print("--------------------------")
print("Membership Operator")
print("h" in "hello")
print("h" not in "hello")
print("z" not in "hello")