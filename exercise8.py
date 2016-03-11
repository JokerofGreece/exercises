pi = [[0 for x in range(8)] for x in range(8)]
temp = [[0 for x in range(8)] for x in range(8)]
f = open('python.txt')  
lines = f.readlines()  # return a list of lines in file
list_of_elements = []
for line in lines:
    list_of_elements += map(int, line.split())
f.close()
"""protimhsa na valw 0,1 gia na fainetai kalytera alla kai epeidh o 
kwdikas den douleue swsta me ta kena"""
k=0
for x in range(0,8):
	for y in range(0,8):
		temp[x][y]=list_of_elements[y+k]
	k=k+8	



for x in range(0, 4):
    h=7
    e=6
    l=6
    p=5
    m=5
    ee=4
    print (" ")
    for i in range(0,8):
	    for j in range(0,8):
		    print temp[i][j],
	    print (" ")
    for i in range(0,8):
        for j in range (0,8):
            if j==0 and i!=0:
                """kati paei strava edw,to psaxna 3 meres kai 
                den to vrhka"""
                pi[i][j]=temp[7][i]
            if i==0:
                pi[i][j]=temp[h][0]
                h=h-1
            if j==7 and i!=7:
                pi[i][j]=temp[0][i]
            if i==7:
                pi[i][j]=temp[e][7]
                e=e-1
            if j==1 and i>=2 and i<=6:
                pi[i][j]=temp[6][i]
            if i==1 and j>=1 and j<=5:
                pi[i][j]=temp[l][1]
                l=l-1
            if j==6 and i>=1 and i<=5:
                pi[i][j]=temp[1][i]
            if i==6 and j>=2 and j<=6:
                pi[i][j]=temp[p][6]
                p=p-1
            if j==2 and i>=3 and i<=5:
                pi[i][j]=temp[5][i]
            if i==2 and j>=2 and j<=4:
                pi[i][j]=temp[m][2]
                m=m-1
            if j==5 and i>=2 and i<=4:
                pi[i][j]=temp[2][i]
            if i==5 and j>=3 and j<=5:
                pi[i][j]=temp[ee][5]
                ee=ee-1
            if i==4 and j==3:
                pi[i][j]=temp[4][4]
            if i==3 and j==3:
                pi[i][j]=temp[4][3]
            if i==3 and j==4:
                pi[i][j]=temp[3][3]
            if i==4 and j==4:
                pi[i][j]=temp[3][4]
    for i in range(0,8):
        for j in range(0,8):
            temp[i][j]=pi[i][j]
