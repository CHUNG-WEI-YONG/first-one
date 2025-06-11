def discount_system():
    age = int(input("Age:"))
    price_before = int(input("Price :"))
    if age< 12 or age > 60:
        discount = price_before*1/10
    else :
        discount = 0

    total = price_before - discount
       
    print(f'''
Age: {age}
Price before: RM{price_before}
Discount: RM{discount:.2f}
Total: RM{total:.2f}
'''
          )

discount_system()
