def fetch_input():
    print("Enter your car mileage :")
    x = input()
    print("you entered  :", x)
    file = open("bridge.txt", "r")
    t0 = float(file.readline())
    t1 = float(file.readline())
    max_km = float(file.readline())
    file.close()
    estimatedPrice = t0 + t1*(float(x)/max_km)
    print("The estimated price for this mileage is ->", estimatedPrice)
    return (0)

fetch_input()

#faut que jutilise une mesure devaluation du resultat de mon model de linear regression a la fin pour juger du
#resultat (style MSE)