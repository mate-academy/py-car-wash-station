class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.brand = brand
        self.clean_mark = clean_mark


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income = self.calculate_washing_price(car)
                total_income += income
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        clean = self.clean_power - car.clean_mark
        clean_class = clean * car.comfort_class
        clean_class_rite = clean_class * self.average_rating
        price = clean_class_rite / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings + rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
