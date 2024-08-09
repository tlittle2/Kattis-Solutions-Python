"""
Goal: 
5
      x
     / \
    /   \
   /     \
  /       \
 /         \
x           x
 \         /
  \       /
   \     /
    \   /
     \ /
      x

"""

def main():
    x = "x"
    slantL = "/"
    slantR = "\\"
    
    n = int(input())

    print("{}{}".format(" "* (n+1), x))

    for i in range(n):
        print("{}{}{}{}".format(" " * (n-i), slantL," " * (2*i+1), slantR))

    print("{}{}{}".format(x, " " * (n*2 + 1), x))
    

    for i in range(n):
        print("{}{}{}{}".format(" " * (i+1), slantR," " * (2*(n-i)-1), slantL))


    print("{}{}".format(" "* (n+1), x))


if __name__ == "__main__":
    main()
