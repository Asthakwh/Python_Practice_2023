#robo speaker
import os

if __name__ == '__main__':
    print("welcome to robo speaker")
    while True:
        x = input("enter what you waht me to speak: ")
        if x == "q":
            os.system("say 'bye bye friend")
            break
        command = f"say {x}"
        os.system(command)