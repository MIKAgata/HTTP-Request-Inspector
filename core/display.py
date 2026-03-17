from benner import show_banner
import os

def get_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    show_banner()
    print("Starting HTTP Request Inspector...")

if __name__ == "__main__":
    main()