import time
def greet(name):
     times = time.strftime("%Y-%m-%d %H:%M:%S")
     print("Hello " + name +", the date today and time is "+str(times))

greet("Vincent")