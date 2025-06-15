def count_vowels(word):
    a = list(word)
    vowel = []
    number = 0
    for words in word:
        if words == 'a' or words == 'e' or words =='i' or words == 'o' or words == 'u':
            vowel.append(words)
        else:
            print("%s is not a vowels"%words)
    for vowels in vowel:
        number +=1
    print("Input:"+word)
    print("Output:",number)
word = str(input("What is uour number:"))
count_vowels(word)
    
