#calcuate n
p=int(input("enter primary number p: "))
q=int(input("enter primary number q: "))
e=int(input("enter e: "))
m=int(input("enter m: "))
n=(p*q)
print("this is the value of n==>", n)
qn=p-1
qn=qn*(q-1)
print("this is the value of qn ==>", qn)
if 1<e<qn:
     print("on the right way 1<e<qn")
else:
    quit("try again")

calculatekeys=10*qn
calculatekeys=calculatekeys+1
calculatekeys=calculatekeys/e
print("this is the value of d", calculatekeys)

print("public key", e, n)
print("private key", calculatekeys, n)

print("++++++CHIFFREMENT++++++")

c=pow(m, e)%n
print(c)
 
print("++++++DCHIFFREMENT++++++")
#OVER FLOW PROBLEM

t=c**int(calculatekeys)
t=t%n
print(t)
    
    

     
       

