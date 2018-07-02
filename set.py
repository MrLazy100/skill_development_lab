 #definite set

A = set([1,2,3,4])     
B = set([4,5,6,7]) 


#cardinality

C= len(A)
print("Cardinality Of A Is :")
print(C)


M= len(B)
print("Cardinality Of B Is :")
print(M)


#Union

U = A | B               
print("Union Is: ")
print(U)

#Intersection

I = A & B               
print("Intersection Is: ")
print(I)

#Difference

D = A - B               
print("Difference Is: ")
print(D)

#elements in A or B

E = A ^ B               
print("Elements in A or B are: ")
print(E)


#membership testing

print(1 in A)
print(8 in A)

print(100 in B)
print(7 in B)
