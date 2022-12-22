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
