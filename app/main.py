class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.possibility_washing(car):
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        difference_purity = self.clean_power - car.clean_mark
        part_of_price = self.average_rating * car.comfort_class
        coefficient_of_price = part_of_price * difference_purity
        return round(coefficient_of_price / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.possibility_washing(car):
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        all_rates = (self.average_rating * self.count_of_ratings) + rate
        self.average_rating = round(all_rates / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

    def possibility_washing(self, car: Car) -> bool:
        if car.clean_mark < self.clean_power:
            return True
        return False
