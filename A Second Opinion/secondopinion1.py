def main():
  #works on test input, but not on the others
    s = int(input())
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)

    print(f'{h:d} : {m:02d} : {s:02d}')    

if __name__ == "__main__":
    main()
