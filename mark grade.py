def score():
    mark = int(input("Marks:"))
    if mark >=90:
        x = 'A'
    elif 80<= mark < 90:
        x = 'B'
    elif 70<= mark < 80:
        x = 'C'
    elif 60<= mark < 70:
        x = 'D'
    else:
        x= 'F'
    print(f"Input: {mark} → Output: {x}")

score()
