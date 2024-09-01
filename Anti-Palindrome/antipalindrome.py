from string import punctuation

def main():
    string = input()
    chars = [char for char in string if char != ' ' and char not in punctuation] # keep only alphabetic characters from the original input
    
    norm = [c.lower() for c in chars] #normalize all characters to the same case for easier operations

    palindrome = False

    for i in range(len(norm)):
         for j in range(i+2,len(norm)+1): #start at i+2 so we check at least substrings of length 2 or more
            temp = norm[i:j]
            if temp == temp[::-1]: #if substring is the same forwards and backwards, we have a palindrome
               palindrome = True
               break
    
    if palindrome:
        print("Palindrome")
    else:
        print("Anti-palindrome")
