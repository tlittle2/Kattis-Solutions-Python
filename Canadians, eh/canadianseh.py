def main():
    ip = input().split()
    print("Canadian!" if ip[len(ip)-1] == 'eh?' else "Imposter!")

if __name__ == "__main__":
    main()
