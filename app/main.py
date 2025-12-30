class Car:
    def __init__(self, comfort_class: int,
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

    def calculate_washing_price(self, car: list) -> float:
        clean_diff = self.clean_power - car.clean_mark
        price_method = car.comfort_class * clean_diff * self.average_rating
        income = round(price_method / self.distance_from_city_center, 1)
        return income
        pass

    def serve_cars(self, cars: list) -> float:
        washable_cars = []
        final_income = []
        for car in cars:
            if car.clean_mark <= self.clean_power:
                washable_cars.append(car)
        for item in washable_cars:
            final_income.append(self.calculate_washing_price(item))
            self.wash_single_car(item)
        return sum(final_income)

    def wash_single_car(self, car: Car) -> float:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        total = self.average_rating * self.count_of_ratings
        total += rating
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)
        print(f"avg rating {self.average_rating} e {self.count_of_ratings}")
