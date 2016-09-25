import msvcrt
import time
n=5
m=0
x=10
y=0
r=5
g=0
print "press enter to start the game"
raw_input()
s_time=time.time()
print "press a to move right"
while(m<=n):
	key=msvcrt.getch()
	if key=="a":
		m+=1
		print "-->",
print " press s to move down" 
while(y<=x):
	key=msvcrt.getch()
	if key=="s":
		y+=1
		print "                    -->"
print "                   ",
		
while(g<=r):
	key=msvcrt.getch()
	if key=="d":
		g+=1
		print "-->",
print "press d to move right"
time_elapsed=time.time()-s_time
print "Congrats you have finished the Game"
print "time taken is "+str(time_elapsed)
	