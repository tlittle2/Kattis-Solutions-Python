def main():
    ip = input().split()

    count = 0
    for i in ip:
        if "ae" in i:
            count+=1

    if count/len(ip) >= 0.4:
        print("dae ae ju traeligt va")
    else:
        print("haer talar vi rikssvenska")
    

if __name__ == "__main__":
    main()
