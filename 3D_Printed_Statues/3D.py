def main():
    statues= int(input())

    numberOfPrinters= 1
    numberOfStatuesPrinted= 0
    days= 0

    while numberOfStatuesPrinted < statues:
        if (statues-numberOfStatuesPrinted) > numberOfPrinters:
            days+=1
            numberOfPrinters+= numberOfPrinters
        else:
            days+=1
            numberOfStatuesPrinted+= numberOfPrinters

    print(days)
    
if __name__ == "__main__":
    main()
