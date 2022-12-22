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