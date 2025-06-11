import math
def bill():
    bill = float(input("Bill:"))
    people = int(input("People :"))
    payment = bill/people
    whole = math.ceil(payment)
    more = whole*people
    extra = more- bill
    print(f'''
Bill: {bill}
People: {people}

Each pays: RM{payment}
Total collected: {people} × {whole} = {more}
Extra collected: RM{extra}
''')
bill()
    
    
    
        
 
