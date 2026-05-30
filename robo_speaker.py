#robo speaker
import os
# it will speak whatever you want it to speak, and if you want to quit just type q and it will say bye bye friend and exit the program
if __name__ == '__main__':
    print("welcome to robo speaker")
    while True:
        x = input("enter what you waht me to speak: ")
        if x == "q":
            os.system("say 'bye bye friend")
            break
        command = f"say {x}"
        os.system(command)
