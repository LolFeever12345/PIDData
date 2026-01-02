import matplotlib.pyplot as plt

x = []
y = []
z = []
t = []
d = []

with open("data.csv", "r") as file:
    next(file)  # Skip header line
    for line in file:
        line = line.strip()
        if not line:
            continue
        xi, yi, zi, ti, di = line.split(",")
        x.append(float(xi))
        y.append(float(yi))
        z.append(float(zi))
        t.append(float(ti))
        d.append(float(di))
    
plt.figure(figsize=(12,6))
plt.plot(x,y, label="Right Speed", color="blue")
plt.plot(x,z, label="Left Speed", color="red")
plt.plot(x,t, label = "Target", color = "green")
# plt.plot(x,d, label = "Distance", color = "purple")
plt.xlabel("PWM ")
plt.ylabel("Linear Speed (mm/s)")
plt.title("Motor Speed Over PWM")
plt.grid(True)

plt.show()
