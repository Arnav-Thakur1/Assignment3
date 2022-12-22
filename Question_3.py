#Problem3
l_1=list(map(int,input("Enter the numbers separated by space:").split()))

l_2=[]
for e in l_1:
    t=(e,e*e)
    l_2.append(t)

print("\nList containing (n,n^2) is shown below:")
print(l_2)