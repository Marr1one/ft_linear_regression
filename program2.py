def training():
    # read le dataset file et faire une linearregression sur la data
    tab = open("data.csv").read().split('\n')
    tab_km = []
    tab_prices = []
    for x in tab[1:]:
        if (x):
            km,price = x.split(',')
            tab_km.append(int(km))
            tab_prices.append(int(price))
    #ou deux tab avec index liee !


    # mettre ca dans une autre fonction !
    max_km = max(tab_km) 
    normalized_km = []
    for km in tab_km:
        normalized_km.append(km/max_km)
    theta0 = 0
    theta1 = 0
    learning_rate = 0.001
    m = len(tab_km)
    j = 0
    print("Nombre de données :", len(tab_km))
    print("Premier kilométrage :", tab_km[0])
    print("Premier prix :", tab_prices[0])
    print("Prix minimum :", min(tab_prices))
    print("Prix maximum :", max(tab_prices))
    while j < 100000:
        sum_error0 = 0
        sum_error1 = 0
        for i in range (m):
            prediction = theta0 + theta1 * normalized_km[i]
            error = prediction - tab_prices[i]
            sum_error0+= error
            sum_error1+= error * normalized_km[i]
        tmp0 = learning_rate * 1/m * sum_error0
        tmp1 = learning_rate * 1/m * sum_error1
        theta0 -= tmp0
        theta1 -= tmp1
        if j % 5 == 0:
            print(j, theta0, theta1)
        j +=1
    print("j - > ", j)
    print("resultat a la fin de la boucle - > ",theta0)
    print("theta1 - >",theta1)
    return theta0,theta1,max_km


    # envoyer le resultat dans un fichier et le reprendre dans le main.py pour avoir le res !


t0,t1,max_km = training()
file = open("bridge.txt", "w")
file.write(str(t0) + '\n')
file.write(str(t1) + '\n')
file.write(str(max_km) + '\n')
file.close()