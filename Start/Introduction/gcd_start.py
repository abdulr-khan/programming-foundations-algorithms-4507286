# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    while (b != 0):
        #save value of "a" in a temp variable t
        t = a
        #save value of "b" into another variable a
        a = b
        b = t % b
    return a

def gcd2(a, b):
    r = a % b
    if (r == 0):
        ans = b
    else:
        ans = gcd2(b, r)
    return ans     
# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4

print(gcd2(60, 96))  # should be 12
print(gcd2(20, 8))   # should be 4
