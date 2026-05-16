t = int(input("Input the time in seconds: "))

hours = t // 3600
minutes = (t % 3600) // 60
seconds = t % 60

# print result
print("Time is:", hours, ":", minutes, ":", seconds)
