def main():
    diff = 1 
    ip1 = list(input())
    ip2 = list(input())

    for i in range(len(ip1)):
        if ip1[i] != ip2[i]:
            diff+=1
    
    print(diff)

if __name__ == "__main__":
    main()
