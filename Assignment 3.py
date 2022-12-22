#Problem1
input_str=str(input("Enter the string: "))
l1=input_str.split()
l2=[]
for e in l1:
    lower_e=e.lower()
    l2.append(lower_e)
set1=set(l2)
dic1={}
for el in set1:
    count=l2.count(el)
    dic1.update({el:count})
dic2={}       
set2={1,2}
set2.clear()  
list2=[]     
if len(l1)==1:
    
    for elements in input_str:
        list2.append(elements)
   
    for el in list2:
        set2.add(el.lower())
    
    string_l=input_str.lower()
    for elem in set2:
        
        dic2.update({elem:string_l.count(elem)})
    
    print("\nDictionary containing 'Letter':'Letter Count' is shown below:")
    print(dic2)

else:
    print("\nDictionary containing {'Word':'Word Count'} is shown below:")
    print(dic1)

#Problem2
Day=int(input("Enter Date(1-31):"))
Month=int(input("Enter Month(1-12):"))
Year=int(input("Enter Year(1800-2025)"))
if Day>31:
    print("Error input correct date")
    exit()
#Checking for leap year
if (Year%4==0):
    leapyear=True
else:
    leapyear=False
#Defining Month Lengths
if Month in [1,3,5,7,8,10,12]:
    monthlength=31
elif Month in [4,6,9,11]:
    monthlength=30
if Month==2:
    if leapyear:
        monthlength=29
    else:
        monthlength=28

if Day>monthlength:
    print("Error  input a correct date")
    exit()
#Adding a day
if Day<monthlength:
    Day=Day+1
else:
    Day=1
    if Month==12:
        Month=1
        Year=Year+1
    else:
        Month=Month+1

print("The Next date will be",Day,"/",Month,"/",Year)

#Problem3
l_1=list(map(int,input("Enter the numbers separated by space:").split()))

l_2=[]
for e in l_1:
    t=(e,e*e)
    l_2.append(t)

print("\nList containing (n,n^2) is shown below:")
print(l_2)


a=float(input("Enter Grade points to be evaluated: "))

#Problem4
G_P=float(input("Enter Grade points to be evaluated: "))

if 9<G_P<=10:
    print("Your Grade is 'A+' and Outstanding performance")
elif 8<G_P<=9:
    print("Your Grade is 'A' and Excellent performance")
elif 7<G_P<=8:
    print("Your Grade is 'B+' and Very Good performance")
elif 6<G_P<=7:
    print("Your Grade is 'B' and Good performance")    
elif 5<G_P<=6:
    print("Your Grade is 'C+' and Average performance")
elif 4<G_P<=5:
    print("Your Grade is 'C' and Below Average performance")
elif G_P==4:
    print("Your Grade is 'D' and Poor performance")
if G_P<4 or G_P>10:
    print("Error Enter a Grade between 0-10 only")
    exit()

#Problem5
P_prog = "ABCDEFGHIJK"
i = 0
while len(P_prog)-i*2 >= 1:
    print(" "*i, P_prog[0 : len(P_prog) - i*2])
    i += 1

#Problem6
repeat="Y"
dic={}
dic2={}
#List containing Y or N
l1=["Y","y","n","N"]
while repeat=="Y" or repeat=="y":
    
    Name = str(input("Enter student name:"))
    SID = int(input("Enter student SID:"))
    if SID<0:
        print("\nError\nSID can't be negative\n")
    else:
       
        dic.update({SID: Name})
        
        dic2.update({Name:SID})
       
        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break
    elif (not (repeat in l1)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a
#printing the dictionary
print("\nQ.6(a)")
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)
# b
#sorting according to name
print("\nQ.6(b)")
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)

# c
#sorting according to SID
print("\nQ.6(c)")
sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# d
print("\nQ.6(d)")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")

#Problem7
#input from user
Number=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
#printing error message when N<=0
if Number<=0 :
    print("\nError\nNumber of elements in fibonacci series must be integer and greater than zero.")
#code for fibonacci series
else:
    #code for fibonacci series for first 2 elements
    if Number == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif Number == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        #Building logic to get fibonacci series
        a = 1
        b = 1
        # For loop
        for i in range(Number - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        # printing the final fibonacci series
        print(f"\nThe fibonacci series with {Number} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / Number)
        # Till two decimal place
        two_decimal = "{:.2f}".format(average)
        # printing average
        print(f"\nAverage of given fibonacci series is {two_decimal}")

#Problem8
#Given Sets
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
#printing the given sets
print(f"Set1= {Set1}\nSet2= {Set2}\nSet3= {Set3}")
#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:")
set_sym_diff=Set1.symmetric_difference(Set2)
print(set_sym_diff)
#b
#Set1 U Set2
print("\nQ.8(b)")
print("\nA new set of all elements that are 'in only one of the three sets Set1,Set2 and Set3' is:")
Set_u1=Set1.union(Set2)

#Set1 U Set2 U set3
set_uf=Set_u1.union(Set3)

#Set1 I set2
set_i1=Set1.intersection(Set2)

#Set1 I Set2 I Set3
set_if=set_i1.intersection(Set3)

#Set1 I Set2
set_12=Set1.intersection(Set2)

#Set2 I Set3
set_23=Set2.intersection(Set3)

#Set3 I Set1
set_13=Set1.intersection(Set3)

#Final required set
set_f1=set_uf-set_12-set_23-set_13
print(set_f1)
#c
print("\nQ.8(c)")
set_c1=set_12.union(set_23)
set_c2=set_c1.union(set_13)
set_final=set_c2-set_if
print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:")
print(set_final)
#d
#forming a set containing values from 1 to 10
print("\nQ.8(d)")
set_d={1,2}
set_d.clear()
for i in range(1,11):
    set_d.add(i)
set_new=set_d-Set1
#printing final set
print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:")
print(set_new)
#e
print("\nQ.8(e)")
set_e=set_d-set_uf
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.")
print(set_e)