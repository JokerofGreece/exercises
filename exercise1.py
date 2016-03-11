def count(i1,j1):
	#ginetai h katametrhsh vhmatwn
	if i1>i2:
		ori=i1-i2
	else:
		ori=i2-i1
	if j1>j2:
		hor=j1-j2
	else:
		hor=j2-j1
	total=ori+hor
	print "You are far:"
	print total,
	print "squares"
from random import randint
i1=randint(1,10)
j1=randint(1,10)
i2=randint(1,10)
j2=randint(1,10)
player=(i1,j1)
treasure=(i2,j2)
count(i1,j1)
moves=0
if (i1==i2) and (j1==j2):
	#se periptwsh pou mpainan tyxaia oi idies syntetagmenes
	from random import randint
	i2=randint(1,10)
	j2=randint(1,10)
	treasure=(i2,j2)
while player!=treasure:
    direction=raw_input("Enter a direction:up,down,left,right and press Enter!:")
    if direction!=("left") and direction!=("l") and direction!=("right") and direction!=("r") and direction!=("down") and direction!=("d") and direction!=("u") and direction!=("up"):
        print "Invalid direction"
        continue
    if i1==1 and (direction=="left" or direction=="l"):
	    print "You can't go left"
	    continue
    if i1==10 and (direction=="right" or direction=="r"):
	    print "You can't go right"
	    continue
    if j1==1 and (direction=="down" or direction=="d"):
	    print "You can't go down"
	    continue
    if j1==10 and (direction=="up" or direction=="u"):
	    print "You can't go up"
	    continue
    if direction=="left" or direction=="l":
        i1=i1-1
    if direction=="right" or direction=="r":
        i1=i1+1
    if direction=="down" or direction=="d":
        j1=j1-1
    if direction=="up" or direction=="u":
	    j1=j1+1
    moves=moves+1    
    count(i1,j1)
    player=(i1,j1)
print "You have reached the treasure!Congratulations!It took you",
print moves,
print "moves"
