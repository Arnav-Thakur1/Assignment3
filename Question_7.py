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