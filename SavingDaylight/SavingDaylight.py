#/usr/bin/env python3

def main():
    month, day, year, time1, time2= input().split() 

    month= str(month)
    day= int(day)
    year= int(year)
    time1Hour, time1Minute= int(input().split(time1, ":"))
    time2Hour, time2Minute= int(input().split(time2, ":"))

    print(time1Hour,time1Minute)

    '''
    hours= time1Hour + time2Hour
    minutes= time1Minute + time2Minute
    print(month + " " + day + " " + year + hours + " hours" + minutes + " minutes")
    '''
if __name__ == "__main__":
    main()