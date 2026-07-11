import time 

def count_down(t):
    while t:
        mins , secs = divmod(t,60)
        timer ='{:02d}:{:02d}'.format(mins, secs)
        print(timer, end ="\r")
        time.sleep(1)
        t -= 1
print(" ____________________________ITS A TIMER______________________ ")
print("__________________________RULES_____________________________\n____________YOU NEED TO ENTER TIME IN SECONDS___________________")
t = input("Enter the time in seconds: ")
count_down(int(t))
