class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        washing_price = (car.comfort_class
                         * (self.clean_power - car.clean_mark)
                         * self.average_rating
                         / self.distance_from_city_center)
        return washing_price

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        marks = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                marks.append(self.clean_power)
            else:
                marks.append(car.clean_mark)
        print(marks)
        return round(income, 1)

    def rate_service(self, rating: float) -> None:
        self.average_rating = round((self.average_rating
                                     * self.count_of_ratings
                                     + rating)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
        print(self.average_rating)
        print(self.count_of_ratings)
# wash_station = CarWashStation(
#     distance_from_city_center=5,
#     clean_power=6,
#     average_rating=2.4,
#     count_of_ratings=11
# )
#
#
# bmw = Car(comfort_class=3, clean_mark=7, brand='BMW')
# audi = Car(comfort_class=4, clean_mark=2, brand='Audi')
#
# mycars = [bmw, audi]
#
# print(wash_station.serve_cars(mycars))













