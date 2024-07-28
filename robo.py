import os
if __name__ == "__main__":
    print("Welcome to the Robo Speaker 2.0 Created by Ayush")
    while True :
        x=input("Enter what you want to pronounce :")
        if x=='q':
           os.system("say 'bye bye friends ")
           break
        command=f"say {x}"
        os.system(command)