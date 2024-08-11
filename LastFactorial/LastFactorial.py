def factorial(x):
    if x== 1:
        return 1
    else:
        return (x * factorial(x-1))

        
def main():
    testCase= int(input())

    for _ in range(testCase):
        testInput= int(input())
        print(factorial(testInput) % 10)

if __name__ == "__main__":
    main()
