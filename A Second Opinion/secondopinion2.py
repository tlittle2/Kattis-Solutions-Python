import datetime

def main():
  #doesn't work beyond 24 hours -> starts to show days in there
    print(str(datetime.timedelta(seconds = int(input()))).replace(":", " : "))

if __name__ == "__main__":
    main()
