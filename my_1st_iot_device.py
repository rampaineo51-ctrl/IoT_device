device = input("Device name: ")
checks = int(input("How many checks? "))
alerts = 0
total = 0
for i in range(checks):
    temp = int(input("Enter temperature: "))
    total = total + temp
    status = "Fan ON - Alert sent" if temp > 25 else "Fan OFF - All good"
    if temp > 25:
        alerts = alerts + 1
    print(f"{device}: {temp}C - {status}")
print(f"Average temp: {total / checks}C")
print(f"Total alerts sent: {alerts}")