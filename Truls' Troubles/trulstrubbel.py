def emptyDict(ip):
    return {i : 0 for i in ip}

def ifnull(d, v):
  try:
    return d[v]
  except KeyError:
    return 0

def main():
    points = input()
    
    d = emptyDict(points)

    for i in points:
        d[i] +=1
        
        if d[i] >= 11:
            if max(d.values()) - min(d.values()) >= 2 or len(d.keys()) == 1:
                d = emptyDict(points)

    print("{}-{}".format(ifnull(d, 'T'), ifnull(d, 'H')))
    
if __name__ == "__main__":
    main()
