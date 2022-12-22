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