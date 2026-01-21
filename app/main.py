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

    def serve_cars(self, cars: list) -> float:
        total_cost = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_cost.append(self.calculate_washing_price(car))
                self.wash_single_car(car)
            else:
                total_cost.append(0)
        total_income = sum(total_cost)
        return total_income

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def calculate_washing_price(self, car: Car) -> float:
        price = []
        difference = (self.clean_power - car.clean_mark)
        washing_price = (car.comfort_class * (difference) * self.average_rating
                         / self.distance_from_city_center)
        price.append(washing_price)
        income = round((sum(list(price))), 1)
        return income

    def rate_service(self, rate: float) -> float:
        sum_of_rates = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round(((sum_of_rates + rate)
                                     / self.count_of_ratings), 1)
