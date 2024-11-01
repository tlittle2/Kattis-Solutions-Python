def main():
    mantra = "Úllen dúllen doff kikke lane koff koffe lane bikke bane úllen dúllen doff.".split()

    int(input())

    friends = input().split()

    print(friends[len(mantra) % len(friends)-1])

if __name__ == "__main__":
    main()
