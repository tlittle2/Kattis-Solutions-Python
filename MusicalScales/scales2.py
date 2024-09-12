def main():
    scales = {
        'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
        'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
        'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
        'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
        'F': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
        'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
        'A#': ['A#' , 'C', 'D', 'D#', 'F', 'G', 'A'],
        'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
        'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
        'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
        'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
        }
    
    int(input())
    notes = set([i for i in input().split()])
    ans = set([k for k,v in scales.items() if notes.issubset(v)])
        
    if len(ans) == 0:
        print("none")
    else:
        for i in sorted(ans):
            print(i, sep = "", end =" ")
            

if __name__ == "__main__": 
    main()
