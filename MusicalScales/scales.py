#!/usr/bin/env python3


#A , A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯


def main():
    scales = [
          ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#',]
        , ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
        , ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        , ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
        , ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
        , ['F', 'G', 'A', 'A#', 'C', 'D', 'E']
        , ['G', 'A', 'B', 'C', 'D', 'E', 'F#']

        , ['A♯' , 'C', 'D', 'D♯', 'F', 'G', 'A']
        , ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#']
        , ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']
        , ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#']
        , ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
          ]


    n = int(input())

    s = set()

    notes = [i for i in input().split()]

    for note in notes:
        s.add(note)

    #print("Set {}".format(s))

    b = False
    srtLst= []
    for scale in scales:
        if s.issubset(scale):
            srtLst.append(scale[0])
            b = True


    if not b:
        print('none')

    else:
        srtLst.sort()
        for i in srtLst:
            print(i, sep = "", end =" ")

        



    
            






if __name__ == "__main__":
    main()