print("Hello World")


def mex(Set):
    Mex = 0

    while (Mex in Set):
        Mex += 1

    return (Mex)


# g(n)=mex({g(n−2)}∪{g(i−2)⊕g(n−i−1)∣2≤i≤n−1}).

def calculateGrundy(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 0

    Set = set()

    Set.add(calculateGrundy(n-2))

    for i in range(2, n):
        tempset = set()
        tempset.add(calculateGrundy(i-2))
        tempset.add(calculateGrundy(n-i-1))
        Set.add(tempset)

    print(Set)
    return (mex(Set))


# Driver program to test above functions
n = 3
calculateGrundy
print(calculateGrundy(n))
