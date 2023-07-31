class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, *args):
        count_car_list = []
        for car in args[0]:
            if self.clean_power > car.clean_mark:
                count_price = self.calculate_washing_price(car)
                self.wash_single_car(car)
                count_car_list.append(count_price)
        count_car = sum(count_car_list)
        print(count_car_list)
        return count_car

    def calculate_washing_price(self, car: Car):
        count = ((car.comfort_class * (
                self.clean_power - car.clean_mark)) * self.average_rating) / self.distance_from_city_center
        return round(count, 1)

    # def serve_cars(self, *args):
    #         if args[0].clean_mark < self.clean_power:
    #             income = self.calculate_washing_price(args[0])
    #         return income

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            self.clean_power = car.clean_mark

    def rate_service(self, number):
        rate = (self.count_of_ratings * (self.average_rating + number)) / (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        return rate


# wash_station = CarWashStation(
#     distance_from_city_center=5,
#     clean_power=7,
#     average_rating=3.5,
#     count_of_ratings=6
# )


wash_station = CarWashStation(
    distance_from_city_center=3,
    clean_power=8,
    average_rating=4.2,
    count_of_ratings=11
)

# wash_station = CarWashStation((3, 9, 4.2, 11), 22.4)


bmw = Car(
    comfort_class=2,
    clean_mark=3,
    brand="BMW",
)

ford = Car(
    comfort_class=2, clean_mark=9, brand='Ford'

)
car_list = [bmw,ford]

print(wash_station.serve_cars(car_list))

# print(wash_station.calculate_washing_price(bmw))
# # # (coun_ofrating * average_rating  + x(new_rate)) / (count_of_rating + 1)

# audit = Car(
#     comfort_class=2, clean_mark=4, brand='BMW'
# )
# print(wash_station.serve_cars(audit))


