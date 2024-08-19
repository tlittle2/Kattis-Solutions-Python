def main():
    alter = {
        "A#" : "Bb",
        "C#" : "Db",
        "D#" : "Eb",
        "F#" : "Gb",
        "G#" : "Ab"
    }
    counter = 1
    while True:
        string = input().split()
        if len(string) == 0:
            break
        
        key = string[0]
        scale = string[1]
        
        b = False

        for k, v in alter.items():
            if k == key:
                print("Case {}: {} {}".format(counter,v,scale))
                b = True
            elif v == key:
                print("Case {}: {} {}".format(counter,k,scale))
                b = True
        
        if not b:
            print("Case {}: UNIQUE".format(counter))

        counter +=1

if __name__ == "__main__": 
    main()
