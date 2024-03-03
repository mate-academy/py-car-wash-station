class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class  # from 1..7
        self.clean_mark = clean_mark        # muddy 1..10 clean
        self.brand = brand
        return


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,  # from 1.0...10.0
                 clean_power: int,                  # clean_mark
                 average_rating: float,             # from 1.0...10.0
                 count_of_ratings: int
                 ) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars_list: list) -> float:
        wash_income = 0
        for car in cars_list:
            if car.clean_mark < self.clean_power:
                wash_income += self.calculate_washing_price(car)
                print(self.calculate_washing_price(car))
            self.wash_single_car(car)
        return round(wash_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return car.comfort_class * (self.clean_power - car.clean_mark) *\
            self.average_rating / self.distance_from_city_center

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return

    def rate_service(self, rating: int) -> None:
        self.average_rating =\
            round((self.average_rating
                  * self.count_of_ratings + rating)
                  / (self.count_of_ratings + 1),
                  1)
        self.count_of_ratings += 1
        return

# first test *****************************************
# bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
# audi = Car(comfort_class=4, clean_mark=9, brand='Audi')
# print("bmw = Car(comfort_class=3, clean_mark=3, brand='BMW') \n" +
#       "audi = Car(comfort_class=4, clean_mark=9, brand='Audi')")
# print("bmw.clean_mark = 3", bmw.clean_mark)     # 3
#
# wash_station = CarWashStation(
#     distance_from_city_center=5,
#     clean_power=6,
#     average_rating=3.5,
#     count_of_ratings=6
# )
#
# income = wash_station.serve_cars([bmw, audi])
# print("bmw.clean_mark = 3", bmw.clean_mark)     # 3
# print("income = 6.3", income)                   # 6.3
# print("bmw.clean_mark = 6", bmw.clean_mark)     # 6
# print("press esc")
# keyboard.wait("esc")
# # os.system("clear")
#
# second test ****************************************
# bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
# audi = Car(comfort_class=4, clean_mark=2, brand='Audi')
# print("bmw = Car(comfort_class=3, clean_mark=3, brand='BMW') \n" +
#       "audi = Car(comfort_class=4, clean_mark=2, brand='Audi')")
# print(bmw.clean_mark)  # 3
# print(audi.clean_mark) # 2
#
# wash_station = CarWashStation(
#     distance_from_city_center=5,
#     clean_power=6,
#     average_rating=3.5,
#     count_of_ratings=6
# )
# income = wash_station.serve_cars([bmw, audi])
#
# print("income = 17.5",income)                   # 17.5
# print("bmw.clean_mark = 6", bmw.clean_mark)     # 6
# print("audi.clean_mark = 6", audi.clean_mark)   # 6
# print("press esc")
# keyboard.wait("esc")
# third test *****************************************
#
# wash_station = CarWashStation(
#     distance_from_city_center=6,
#     clean_power=8,
#     average_rating=3.9,
#     count_of_ratings=11
# )
#
# print("wash_station.average_rating = 3.9", wash_station.average_rating)
# print("wash_station.count_of_ratings = 11", wash_station.count_of_ratings)
# print("wash_station.rate_service(5)")
# wash_station.rate_service(5)
# print("wash_station.average_rating = 4.0", wash_station.average_rating)
# print("wash_station.count_of_ratings = 12", wash_station.count_of_ratings)
# keyboard.wait("esc")
# fourth test ***************************************

# bmw = Car(3, 3, 'BMW')
# audi = Car(4, 9, 'Audi')
# mercedes = Car(7, 1, 'Mercedes')
# ws = CarWashStation(6, 8, 3.9, 11)
#
# income = ws.serve_cars([bmw, audi, mercedes])
#
# print("income = 41.7", income)                          # 41.7
# print("bmw.clean_mark = 8", bmw.clean_mark)             # 8
# print("audi.clean_mark = 9", audi.clean_mark)           # 9
# print("mercedes.clean_mark = 8", mercedes.clean_mark)   # 8
# audi wasn't washed
# all other cars are washed to '8'
#
# ford = Car(2, 1, 'Ford')
# wash_cost = ws.calculate_washing_price(ford)
# only calculating cost, not washing
# print("Ford wash_cost = 9.1", wash_cost)            #9.1
# print("ford.clean_mark = 1", ford.clean_mark)      #1
#
# ws.rate_service(5)

# ws.count_of_ratings == 12
# ws.average_rating == 4.0
