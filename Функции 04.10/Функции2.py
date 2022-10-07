def points_count(points):
    if points <= 49:
        print("скидка 10%")
    elif points >= 50 and points <= 99:
        print("скидка 15%")
    elif points >= 100:
        print("скидка 20 %")


points = int(input('кол-во баллов'))
points_count(points)
