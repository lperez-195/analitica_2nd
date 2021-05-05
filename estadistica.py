import csv
import statistics
import numpy as np
with open('ulabox_orders_with_categories_partials_2017.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    contador = 0

    cust = []
    order = []
    total = []
    disc = []
    wday = []
    hour = []
    food = []
    fresh = []
    drink = []
    home = []
    beauty = []
    health = []
    baby = []
    pets = []

    for row in spamreader:
        tmpString = ''.join(row)
        newList = tmpString.split(',')
        if newList[0] != '"customer"':
            contador += 1
            cust.append(int(newList[0]))
            order.append(int(newList[1]))
            total.append(int(newList[2]))
            disc.append(float(newList[3]))
            wday.append(int(newList[4]))
            hour.append(int(newList[5]))
            food.append(float(newList[6]))
            fresh.append(float(newList[7]))
            drink.append(float(newList[8]))
            home.append(float(newList[9]))
            beauty.append(float(newList[10]))
            health.append(float(newList[11]))
            baby.append(float(newList[12]))
            pets.append(float(newList[13]))

    meanCust = statistics.mean(cust)
    modeCust = statistics.mode(cust)
    medianCust = statistics.median(cust)
    devstCust = statistics.stdev(cust)

    print("Tamaño del dataset: ", contador)
    print("Min de customer", min(cust))
    print("Max de customer", max(cust))
    print("Mean de customer: ", meanCust)
    print("Mode de customer: ", modeCust)
    print("Median de customer: ", medianCust)
    print("Desviación estándar de customer: ", devstCust)

    print("Q2 quantile de customer : ", np.quantile(cust, .50))
    print("Q1 quantile de customer : ", np.quantile(cust, .25))
    print("Q3 quantile de customer : ", np.quantile(cust, .75))
    print("100th quantile de customer : ", np.quantile(cust, .1))
    print("\n")

    meanOrder = statistics.mean(order)
    modeOrder = statistics.mode(order)
    medianOrder = statistics.median(order)
    devstOrder = statistics.stdev(order)

    print("Min de order", min(order))
    print("Max de order", max(order))
    print("Mean de order: ", meanOrder)
    print("Mode de order: ", modeOrder)
    print("Median de order: ", medianOrder)
    print("Desviación estándar de order: ", devstOrder)

    print("Q2 quantile de order : ", np.quantile(order, .50))
    print("Q1 quantile de order : ", np.quantile(order, .25))
    print("Q3 quantile de order : ", np.quantile(order, .75))
    print("100th quantile de order : ", np.quantile(order, .1))
    print("\n")

    meanTotal = statistics.mean(total)
    modeTotal = statistics.mode(total)
    medianTotal = statistics.median(total)
    devstTotal = statistics.stdev(total)

    print("Min de total", min(total))
    print("Max de total", max(total))
    print("Mean de total: ", meanTotal)
    print("Mode de total: ", modeTotal)
    print("Median de total: ", medianTotal)
    print("Desviación estándar de total: ", devstTotal)
    
    print("Q2 quantile de total : ", np.quantile(total, .50))
    print("Q1 quantile de total : ", np.quantile(total, .25))
    print("Q3 quantile de total : ", np.quantile(total, .75))
    print("100th quantile de total : ", np.quantile(total, .1))
    print("\n")

    meanDisc = statistics.mean(disc)
    modeDisc = statistics.mode(disc)
    medianDisc = statistics.median(disc)
    devstDisc = statistics.stdev(disc)

    print("Min de discount", min(disc))
    print("Max de discount", max(disc))
    print("Mean de discount: ", meanDisc)
    print("Mode de discount: ", modeDisc)
    print("Median de discount: ", medianDisc)
    print("Desviación estándar de discount: ", devstDisc)

    print("Q2 quantile de discount : ", np.quantile(disc, .50))
    print("Q1 quantile de discount : ", np.quantile(disc, .25))
    print("Q3 quantile de discount : ", np.quantile(disc, .75))
    print("100th quantile de discount : ", np.quantile(disc, .1))
    print("\n")

    meanWday = statistics.mean(wday)
    modeWday = statistics.mode(wday)
    medianWday = statistics.median(wday)
    devstWday = statistics.stdev(wday)

    print("Min de weekday", min(wday))
    print("Max de weekday", max(wday))
    print("Mean de weekday: ", meanWday)
    print("Mode de weekday: ", modeWday)
    print("Median de weekday: ", medianWday)
    print("Desviación estándar de weekday: ", devstWday)

    print("Q2 quantile de weekday : ", np.quantile(wday, .50))
    print("Q1 quantile de weekday : ", np.quantile(wday, .25))
    print("Q3 quantile de weekday : ", np.quantile(wday, .75))
    print("100th quantile de weekday : ", np.quantile(wday, .1))
    print("\n")

    meanHour = statistics.mean(hour)
    modeHour = statistics.mode(hour)
    medianHour = statistics.median(hour)
    devstHour = statistics.stdev(hour)

    print("Min de hour", min(hour))
    print("Max de hour", max(hour))
    print("Mean de hour: ", meanHour)
    print("Mode de hour: ", modeHour)
    print("Median de hour: ", medianHour)
    print("Desviación estándar de hour: ", devstHour)
    print("Q2 quantile de hour : ", np.quantile(hour, .50))
    print("Q1 quantile de hour : ", np.quantile(hour, .25))
    print("Q3 quantile de hour : ", np.quantile(hour, .75))
    print("100th quantile de hour : ", np.quantile(hour, .1))
    print("\n")

    meanFood = statistics.mean(food)
    modeFood = statistics.mode(food)
    medianFood = statistics.median(food)
    devstFood = statistics.stdev(food)

    print("Min de food", min(food))
    print("Max de food", max(food))
    print("Mean de food: ", meanFood)
    print("Mode de food: ", modeFood)
    print("Median de food: ", medianFood)
    print("Desviación estándar de food: ", devstFood)

    print("Q2 quantile de food : ", np.quantile(food, .50))
    print("Q1 quantile de food : ", np.quantile(food, .25))
    print("Q3 quantile de food : ", np.quantile(food, .75))
    print("100th quantile de food : ", np.quantile(food, .1))
    print("\n")

    meanFresh = statistics.mean(fresh)
    modeFresh = statistics.mode(fresh)
    medianFresh = statistics.median(fresh)
    devstFresh = statistics.stdev(fresh)

    print("Min de fresh", min(fresh))
    print("Max de fresh", max(fresh))
    print("Mean de fresh: ", meanFresh)
    print("Mode de fresh: ", modeFresh)
    print("Median de fresh: ", medianFresh)
    print("Desviación estándar de fresh: ", devstFresh)

    print("Q2 quantile de fresh : ", np.quantile(fresh, .50))
    print("Q1 quantile de fresh : ", np.quantile(fresh, .25))
    print("Q3 quantile de fresh : ", np.quantile(fresh, .75))
    print("100th quantile de fresh : ", np.quantile(fresh, .1))
    print("\n")

    meanDrink = statistics.mean(drink)
    modeDrink = statistics.mode(drink)
    medianDrink = statistics.median(drink)
    devstDrink = statistics.stdev(drink)

    print("Min de drink", min(drink))
    print("Max de drink", max(drink))
    print("Mean de drink: ", meanDrink)
    print("Mode de drink: ", modeDrink)
    print("Median de drink: ", medianDrink)
    print("Desviación estándar de drink: ", devstDrink)

    print("Q2 quantile de drink : ", np.quantile(drink, .50))
    print("Q1 quantile de drink : ", np.quantile(drink, .25))
    print("Q3 quantile de drink : ", np.quantile(drink, .75))
    print("100th quantile de drink : ", np.quantile(drink, .1))
    print("\n")

    meanHome = statistics.mean(home)
    modeHome = statistics.mode(home)
    medianHome = statistics.median(home)
    devstHome = statistics.stdev(home)

    print("Min de home", min(home))
    print("Max de home", max(home))
    print("Mean de home: ", meanHome)
    print("Mode de home: ", modeHome)
    print("Median de home: ", medianHome)
    print("Desviación estándar de home: ", devstHome)

    print("Q2 quantile de home : ", np.quantile(home, .50))
    print("Q1 quantile de home : ", np.quantile(home, .25))
    print("Q3 quantile de home : ", np.quantile(home, .75))
    print("100th quantile de home : ", np.quantile(home, .1))
    print("\n")

    meanBeauty = statistics.mean(beauty)
    modeBeauty = statistics.mode(beauty)
    medianBeauty = statistics.median(beauty)
    devstBeauty = statistics.stdev(beauty)

    print("Min de beauty", min(beauty))
    print("Max de beauty", max(beauty))
    print("Mean de beauty: ", meanBeauty)
    print("Mode de beauty: ", modeBeauty)
    print("Median de beauty: ", medianBeauty)
    print("Desviación estándar de beauty: ", devstBeauty)

    print("Q2 quantile de beauty : ", np.quantile(beauty, .50))
    print("Q1 quantile de beauty : ", np.quantile(beauty, .25))
    print("Q3 quantile de beauty : ", np.quantile(beauty, .75))
    print("100th quantile de beauty : ", np.quantile(beauty, .1))
    print("\n")

    meanHealth = statistics.mean(health)
    modeHealth = statistics.mode(health)
    medianHealth = statistics.median(health)
    devstHealth = statistics.stdev(health)

    print("Min de health", min(health))
    print("Max de health", max(health))
    print("Mean de health: ", meanHealth)
    print("Mode de health: ", modeHealth)
    print("Median de health: ", medianHealth)
    print("Desviación estándar de health: ", devstHealth)

    print("Q2 quantile de health : ", np.quantile(health, .50))
    print("Q1 quantile de health : ", np.quantile(health, .25))
    print("Q3 quantile de health : ", np.quantile(health, .75))
    print("100th quantile de health : ", np.quantile(health, .1))
    print("\n")

    meanBaby = statistics.mean(baby)
    modeBaby = statistics.mode(baby)
    medianBaby = statistics.median(baby)
    devstBaby = statistics.stdev(baby)
    
    print("Min de baby", min(baby))
    print("Max de baby", max(baby))
    print("Mean de baby: ", meanBaby)
    print("Mode de baby: ", modeBaby)
    print("Median de baby: ", medianBaby)
    print("Desviación estándar de baby: ", devstBaby)

    print("Q2 quantile de baby : ", np.quantile(baby, .50))
    print("Q1 quantile de baby : ", np.quantile(baby, .25))
    print("Q3 quantile de baby : ", np.quantile(baby, .75))
    print("100th quantile de baby : ", np.quantile(baby, .1))
    print("\n")

    meanPets = statistics.mean(pets)
    modePets = statistics.mode(pets)
    medianPets = statistics.median(pets)
    devstPets = statistics.stdev(pets)

    print("Min de pets", min(pets))
    print("Max de pets", max(pets))
    print("Mean de pets: ", meanPets)
    print("Mode de pets: ", modePets)
    print("Median de pets: ", medianPets)
    print("Desviación estándar de pets: ", devstPets)

    print("Q2 quantile de pets : ", np.quantile(pets, .50))
    print("Q1 quantile de pets : ", np.quantile(pets, .25))
    print("Q3 quantile de pets : ", np.quantile(pets, .75))
    print("100th quantile de pets : ", np.quantile(pets, .1))
    print("\n")
