def main():
    thres, loop = map(int, input().split())
    s= 0
    ans = 0
    
  for _ in range(loop):
        status, num= input().split()
        status= str(status)
        num= int(num)
        if status == "enter":
            if s+num > thres:
                ans+=1
            else:
                s+=num
        else:
            s-=num
    print(ans)
  
if __name__ == "__main__":
    main()
