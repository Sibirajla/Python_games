value = ""
print("""
Enter Start to start the program
Stop to Stop the program
Quit to end The Program
""")
started = 0
while True:
    value = input(">> ").lower()
    if value == "start":
        if started:
            print("Car Engine Already Started")
        else:
            started = 1
            print("Car engine started")
    elif value == "stop":
        if not started:
            print("Engine already Stopped")
        else:
            started = 0
            print("Engine has been Stopped")
    elif value == "quit":
        exit()
    else:
        print("Enter Correct Value")
