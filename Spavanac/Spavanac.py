def main():
    hour, minute= map(int, input().split())
    newMinute= minute - 45
    
    hour = hour-1 if newMinute < 0 else hour
        
    print(hour%24, newMinute%60)
    

if __name__ == "__main__": 
    main()
