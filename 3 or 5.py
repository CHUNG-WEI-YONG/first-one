#📝 Problem Statement
#Write a function that takes an integer n and returns the sum of all natural numbers less than n that are multiples of 3 or 5.


def sum_number():
    i = int(input("What is your number? \n >>"))
    list3and5 = []
    n = 0
    for number in range(1 , i+1):
        if number %3 == 0 or number%5 ==0:
            list3and5.append(number)
        else:
            print(number,"is not a multiples of three and five")
    for multiples in list3and5:
        n+=multiples
    print("Input: n =",i)
    print("Output: ",n)


sum_number()
