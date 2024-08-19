import time
import sys
import random

def animate_logo():
    logo = """
    SSS  H   H   OOO   JJJJ III  BBB 
    S    H   H  O   O    J  III  B  B
    SSS  HHHHH  O   O    J  III  BBB 
      S  H   H  O   O  J J  III  B  B
    SSS  H   H   OOO   JJJ  III  BBB 
    """
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    clear_screen = '\033[2J\033[H'
    
    for i in range(5):
        color = random.choice(colors)
        sys.stdout.write(clear_screen)
        sys.stdout.write(f"{color}{logo}\033[0m")
        sys.stdout.flush()
        time.sleep(0.5)

if __name__ == '__main__':
    animate_logo()
    num = input("Enter Number: ")
    amt = input("Enter Limit: ")

    try:
        amt = int(amt)
        nagad = bomber(num, amt)
    except ValueError:
        print(json.dumps({"error": "Invalid 'amt' parameter."}, indent=4, ensure_ascii=False))