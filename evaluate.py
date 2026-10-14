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


mse = 0

for i in range(len(tab_km)):
    predict = theta0 + theta1 * (tab_km[i]/max_km)
    error = predict - tab_prices[i]
    mse += error ** 2

mse = mse/len(tab_km)

print("MSE : ", mse)
print("RMSE:", mse ** 0.5)
