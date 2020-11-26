#Get Index of the players
def index_player(arr,player,pawn):
    print(player,pawn)
    index1=0
    for i in arr:
        try:
            index2=i.index(str(str(player)+'-'+str(pawn)))
        except ValueError:
            index1=index1+1
            continue
    return index1,index2
rows, cols = (5, 5)
player_flag=True
arr = [['-' for i in range(cols)] for j in range(rows)] 
p1=str(input()).split(",")
p2=str(input()).split(",")
flag=True
for i in range(0,len(arr[0])):
    arr[4][i]=str('A-'+str(p1[i]))
    arr[0][i]=str('B-'+str(p2[i]))
while(flag):
    pawn,move=str(input()).split(":")
    if(player_flag==True):
        player='A'
    else:
        player='B'
    index1,index2=index_player(arr,player,pawn)
    print(index1,index2)
    print(move)
    if(player_flag==True):
        if(index1==0 or index1==4):
            if(move=='R'):
                if(arr[index1][index2+1]=='-'):
                    temp=arr[index1][index2]
                    arr[index1][index2]='0'
                    arr[index1][index2+1]=temp
            elif(move=='F'):
                print(arr[index1][index2])
                if(arr[index1-1][index2]=='-'):
                    temp=arr[index1][index2]
                    arr[index1][index2]='0'
                    arr[index1-1][index2]=temp
            else:
                print("Invalid Move ... Move Again")
                player_flag=True
        elif(not (index1==0 or index1==4)):
            if(move=='F'):
                print(arr[index1][index2])
                if(arr[index1-1][index2]=='-'):
                    temp=arr[index1][index2]
                    arr[index1][index2]='0'
                    arr[index1-1][index2]=temp
            else:
                print("Invalid Move ... Move Again") 
                player_flag=True 
    print(arr)
