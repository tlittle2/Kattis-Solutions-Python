def main():
  n = int(input())
  binary_reversed = bin(n)[2:][::-1]
  result = int(binary_reversed, 2)
  print(result)

if __name__ == "__main__":
  main()
