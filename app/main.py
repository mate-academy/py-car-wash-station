# Доброго дня!  мене виникла проблема із завданням linter-formater. Саму тему з list-comprahantion я засвоїв,
# а із задачою не можу розібратися. Чи не могли б ви показати мені як її робити? Задачу закинув у папку
# need_help. Дякую!


class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, count_of_cars: list) -> int:
        income = 0
        for car in count_of_cars:
            if car.clean_mark <= self.clean_power:
                income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: classmethod) -> int:
        calculation_price = car.comfort_class * \
            (self.clean_power - car.clean_mark) * \
            self.average_rating / self.distance_from_city_center
        return round(calculation_price, 2)

    def wash_single_car(self, car: classmethod) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        else:
            print("Sorry, but your car is clean enough!")

    def rate_service(self, rating_of_one_service: int) -> None:
        calculation_of_rating = ((self.average_rating * self.count_of_ratings)
                                 + rating_of_one_service) / (self.count_of_ratings + 1)
        self.average_rating = round(calculation_of_rating, 1)
        self.count_of_ratings += 1
