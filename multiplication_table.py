for row in range(1, 13):
    print(*(f"{row*col:3}" for col in range(1, 13)))