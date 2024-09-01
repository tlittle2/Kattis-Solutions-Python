import datetime

def main():
  #test input is right, but fails after the test input
    total_seconds = int(datetime.timedelta(seconds = int(input())).total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"{hours:d} : {minutes:02d} : {seconds:02d}")

if __name__ == "__main__":
    main()
