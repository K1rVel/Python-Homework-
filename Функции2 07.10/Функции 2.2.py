def trip_price():
    a = int(input("расстояние поездки в километрах"))
    meters = a*1000
    basic_price = 4
    price = meters//140
    price2 = price//4
    final_price = price2 + 4
    return final_price


print(trip_price())