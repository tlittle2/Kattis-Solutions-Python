from itertools import zip_longest

def main():
    l = []
    fill = ' '
    n = int(input())
    l = [list(input()) for _ in range(n)] #append all string input from stdin into list
        
    indexed = list(zip_longest(*l, fillvalue=fill)) #match all index 0, index 1, etc up with each other. if the value is null, replace with space

    newWord = ""
    for i in indexed:
        filtered_chars = [char for char in i if char != fill] #get all characters in current indexed list that are not spaces
        
        if filtered_chars:
             newWord += chr(sum(ord(char) for char in filtered_chars) // len(filtered_chars)) #get ascii number of filtered, and convert to the character
        else:
            newWord += fill #otherwise just add space
            
    print(newWord)

if __name__ == "__main__":
    main()
