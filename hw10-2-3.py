def three_letter_words(lst):
    total = 0 
    length = 0 
    for x in lst:
        length = len(x)
        if length == 3:
            total += 1 
    return(total)

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)
