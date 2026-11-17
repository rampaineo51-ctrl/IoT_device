device = input("Device name: ")
for i in range(2):
    temp = int(input("Enter temperature: "))
    status = "Fan ON - Alert sent" if temp > 25 else "Fan OFF - All good"
    print(f"{device}: {temp}C - {status}")