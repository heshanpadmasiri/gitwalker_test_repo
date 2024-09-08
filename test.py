#! env/bin/python3
import sys 

if __name__ == '__main__':
    with open("state.txt", "r") as f:
        state = f.read().strip() == "working"
        print("working" if state else "not working")
        sys.exit(0 if state else 1)
