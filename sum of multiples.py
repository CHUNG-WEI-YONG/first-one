def sum_multiples(n):
    list = []
    num = range(0,n)
    total = 0
    for i in num:
        if i%3 == 0 or i%5 ==0:
            list.append(i)
            total +=i
    print("Input:",n)
    print("Output:",total)

n = int(input("What is your number?\n"))
sum_multiples(n)
print(n)

