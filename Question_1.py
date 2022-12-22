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