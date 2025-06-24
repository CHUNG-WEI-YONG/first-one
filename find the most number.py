from collections import Counter

def mst_number():
    
    a = []
    while True:
        num = input("Enter the number:('K'to stop)")
        if str(num).lower() =="k":
            break
           
        else:
            try:
                num = int(num)
                a.append(num)
            except ValueError :
                print("Please enter a number or 'k'")
    n = len(list(a))
    most = int(n/2)
    dict1 = Counter(a)
    for number,time in dict1.items():
        if time > most:
            print(f"Majority Element is {number}, appearing{time} times.")
        elif time < most:
            print(f"{number}Not majority")


mst_number()


