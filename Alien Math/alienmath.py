import re

def main():
    d={}

    base = int(input())
    i = 0
    for word in input().split():
        d[word] = i
        i+=1

    split_values = sorted(d.keys(), key=len, reverse=True)

    pattern = '|'.join(map(re.escape, split_values)) #create dynamic regex pattern for finding occurrences of strings that are in the map

    result = re.split(f"({pattern})", input()) # when occurrences are found, split what is found into its own string

    split_result = [s for s in result if s] # remove the spaces from the result list

    length = len(split_result)

    ans = 0
    for i in split_result:
        ans += d[i] * base**(length-1)
        length-=1

    print(ans)
    


if __name__ == "__main__":
    main()
