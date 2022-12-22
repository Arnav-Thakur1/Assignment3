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