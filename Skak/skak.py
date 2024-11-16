def main():
    petra = set(map(int, input().split()))
    gardar = set(map(int, input().split()))

    print(1 if petra.intersection(gardar) else 2)
                        
if __name__ == "__main__":
    main()
