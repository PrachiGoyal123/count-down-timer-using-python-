import time

def countdown(t_time):
    while t_time:
         mins,secs = divmod(t_time,60)        
         timer = '{:02d}:{:02d}'.format(mins,secs) 
         print(timer,end="\r") 
         time.sleep(1)
         t_time -=1

    print(" \n oop's!!! Time is completed ")
     
t_time = input("Enter the time in seconds : ")

countdown(int(t_time))



