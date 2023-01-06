# File:chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    N = eval(input("How many numbers should I print?"))
    n = eval(input("Enter a number between 0 and 1:"))
    for i in range(N):
             n = 3.9*n*(1-n)
             print(n)
main()
