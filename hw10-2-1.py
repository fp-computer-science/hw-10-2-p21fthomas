

lst1 = []
def count_odds(L):
    for x in [2, 4, 6, 8, 9]:
        if x % 2 != 0:
            lst1.append(x)
count_odds(lst1)
print(lst1)

lst2 = []
def count_odds(L):
    for x in [1, 3, 5, 7, 9]:
        if x % 2 != 0:
            lst2.append(x)
count_odds(lst2)
print(lst2)

lst3 = []
def count_odds(L):
    for x in [2, 4, 6, 8, 10]:
        if x % 2 != 0:
            lst3.append(x)
count_odds(lst3)
print(lst3)

