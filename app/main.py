class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        try:
            if comfort_class > 7 or comfort_class < 1:
                raise ValueError("invalid class value")
        except ValueError as class_value_error:
            print(class_value_error)
        try:
            if clean_mark > 10 or clean_mark < 1:
                raise ValueError("invalid clean_mark")
        except ValueError as clean_mark_value_error:
            print(clean_mark_value_error)




class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_rating + rating)
                                    / self.count_of_ratings, 1)


bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')

print(bmw.clean_mark)  # 3

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

income = wash_station.serve_cars([bmw, audi])

print(income)  # 6.3
print(bmw.clean_mark)  # 6