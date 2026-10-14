import matplotlib.pyplot as plt

tab_km = []
tab_prices = []

with open("data.csv", "r") as file:
    next(file)
    for line in file:
        if line.strip():
            km,price = line.strip().split(",")
            tab_km.append(float(km))
            tab_prices.append(float(price))

with open("bridge.txt", "r") as file:
    theta0 = float(file.readline())
    theta1 = float(file.readline())
    max_km = float(file.readline())

predicted_prices = []

for km in tab_km:
    predicted = theta0 + theta1 * (km/max_km)
    predicted_prices.append(predicted)


plt.scatter(tab_km,tab_prices,label ="Real prices")
plt.plot(tab_km, predicted_prices,color="red",label="Linear Regression")
plt.xlabel("Mileage(km)")
plt.ylabel("Price(Euros)")
plt.legend()
plt.show()