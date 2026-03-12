def show_banner():
    with open("asscii.txt", "r") as f:
        print(f.read())

def main():
    show_banner()
    print("Starting HTTP Request Inspector...")

# if __name__ == "__main__":
#     main()