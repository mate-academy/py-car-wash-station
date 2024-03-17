class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        self.wash_ability = None


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float | int,
                 clean_power: int,
                 average_rating: float | int,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = round(distance_from_city_center, 1)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def wash_ability(self, car: Car) -> bool:
        if car.clean_mark >= self.clean_power:
            car.wash_ability = False
            print(f"Can't wash {car.brand} with {car.clean_mark} mark")
        else:
            car.wash_ability = True
        return car.wash_ability

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.wash_ability(car):
                income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car : Car) -> float:
        if car.clean_mark < self.clean_power:
            diff_clean = self.clean_power - car.clean_mark
            coeff = self.average_rating / self.distance_from_city_center
            price = car.comfort_class * diff_clean * coeff
            return round(price, 1)
        return f"Can't calculate price for {car.brand}"

    def wash_single_car(self, car: Car) -> None:
        if car.wash_ability:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float | int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings
             + rate) / (self.count_of_ratings + 1)
            , 1)
        self.count_of_ratings += 1
