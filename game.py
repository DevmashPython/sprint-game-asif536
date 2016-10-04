import msvcrt
import time
 
n=6
x=11
r=6
y=0
g=0
print " Press enter key to start the game"

raw_input()
s_time=time.time()
print "Press d to move right"

while(1):
	key=msvcrt.getch()
	if key=="d":
		y+=1
		print "-->" ,
		if y==n:
			print " Press s to Move down."
			break
	else:
		print "You lost the game!"
		exit(1)
while(1):
	key1=msvcrt.getch()
	if key1=="s":
		y+=1
		print "                      | "
		print "                      | "
		print "                      V "
		if y==x:
			print "Press d to Move right." ,
			break
	else:
		print "You lost the game!"
		exit(1)     
while(1):
	key2=msvcrt.getch()
	if key2=="d":
		g+=1
		print "-->" ,
		if g==r:
			break
	else:
		print "You lost the game!"
		exit(1)

time_elapsed=time.time()-s_time
print "Congrats you have finished the game!"
print "Time taken is "+str(time_elapsed)

''' 
No improvements required!
'''
