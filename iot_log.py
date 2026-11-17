device = input("Device name: ")

with open("iot_log.txt", "a") as log:
    for i in range(2):
        temp = int(input("Enter temperature: "))
        status = "Fan ON - Alert sent" if temp > 25 else "Fan OFF - All good"
        line = f"{device}: {temp}C - {status}"
        print(line)
        log.write(line + "\n")

print("Saved to iot_log.txt")