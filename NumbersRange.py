def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def sum_of_devisors(n):
    total = 0
    i = 1
    while n > 0:
        if n % i == 0:
            total += i
            n = n/i
        i += 1


def is_perfect(num):
    total = sum_of_devisors(num)
    if num == total:
        return True
    return False


def is_abundant(n):
    if sum_of_devisors(n) > n:
        return True
    return False


def menu():
    print("\nMain Menu\n")
    print("1 - Find all prime numbers within a given range")
    print("2 - Find all perfect numbers within a given range")
    print("3 - Find all abundant numbers within a given range")
    print("4 - Chart all even, odd, prime, perfect and abundant numbers within a given range")
    print("5 - Quit")

    userChoice = int(input("\nYour Choice: "))


#validate
    if userChoice > 5 or userChoice < 1:
        print("Invalid, try again")
        return menu()
    return userChoice


def get():

    start = int(input("Enter starting number (positive only): "))
    while start<0:
        print("Invalid, try again")
        start=int(input("Enter starting number (positive only): "))
    end=int(input("Enter ending number: "))

    while end<start:
        print("Invalid, try again")
        end = int(input("Enter ending number: "))
    return (start, end)



def main():
    userChoice = menu()
    while userChoice != 5:
        a, b = get()

        if userChoice == 1:
            print(f"\nAll prime numbers between {a} and {b}")
            print("#"*20)

            for i in range(a, b+1):
                if is_prime(i):
                    print(i)
            print("#"*20)

        elif userChoice == 2:
            print(f"\nAll perfect numbers between {a} and {b}")
            print("#"*20)

            for i in range(a, b+1):
                if is_perfect(i):
                    print(i)
            print("#"*20)

        elif userChoice == 3:
            print(f"\nAll abundant numbers between {a} and {b}")
            print("#"*20)
            for i in range(a, b+1):
                if is_abundant(i):
                    print(i)
            print("#"*20)

        elif userChoice == 4:
            print(f"\nAll prime numbers between {a} and {b}")
            print("#"*20)
            for i in range(a, b+1):
                if is_prime(i):
                    print(i)
            print("#"*20)
            print(f"\nAll perfect numbers between {a} and {b}")
            print("#"*20)

            for i in range(a, b+1):
                if is_perfect(i):
                    print(i)
            print("#"*20)
            print(f"\nAll abundant numbers between {a} and {b}")
            print("#"*20)

            for i in range(a, b+1):
                if is_abundant(i):
                    print(i)
            print("#"*20)
        userChoice = menu()

main()

