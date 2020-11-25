
import time, socket, sys
import random
balls={
    "full toss": 4,
    "Yorker": 3,
    "Out-swinger": 3,
    "In-swinger": 2,
    "Bouncer": 4,
    "Slower Ball":2
}
shots={
    "Defend": [5,0],
    "Run": [7,1],
    "Run Fast": [6,2], 
    "Cover Drive": [7,2],
    "On Drive": [5,2],
    "Straight Drive": [6,2],
    "Square Cut": [7,4],
    "Pull": [8,4],
    "Hook": [7,6],
    "Helicopter": [8,6]
}
balls_shots={
    "full toss": "Defend,Run,Run Fast,Square Cut,Helicopter",
    "Yorker": "Defend,Run,Straight Drive,Square Cut,Hook",
    "Out-swinger":"Defend,Run,Cover Drive,Pull,Helicopter",
    "In-swinger": "Defend,Run,On Drive,Pull,Hook",
    "Bouncer": "Defend,Run,Cover Drive,Pull,Hook",
    "Slower Ball":"Defend,Run,On Drive,Pull,Helicopter"
}
overs=0
max_balls=18
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
conn.send(name.encode())

curr=0
last=0
overs=1
while True:
    while True:
        ball=random.choice(list(balls_shots.keys()))
        ball_modifier=balls[ball]
        shots_disp=balls_shots[ball].split(",")
        message = """ 
        Current Runs: """+str(curr)+"""
        Runs on last ball: """+str(last)+"""
        Current Ball : """+str(overs)+"""
        Possible Shots:+"""
        for i in shots_disp:
            prob=(((shots[i][0] - ball_modifier) * 100) / shots[i][0])
            message=message+"\n"+str(i)+"-"+str(shots[i][1])+"-"+str(prob)+"\n"
        if overs==max_balls:
            message = "Thanks for playing"
            conn.send(message.encode())
            print("\n")
            break
        conn.send(message.encode())
        shot = conn.recv(1024)
        shot = shot.decode()
        runs=shots[shot][1]
        if(runs!=0):
            conn.send(("YOU HIT A "+str(runs)).encode())
        else:
            conn.send("YOU MISSED".encode())
        curr=curr+runs
        last=runs
        overs=overs+1
        if(overs==max_balls):
            break
        else:
            print(s_name, ":", message)
