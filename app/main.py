class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            income += self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        price1 = car.comfort_class * (self.clean_power - car.clean_mark)
        price2 = self.average_rating / self.distance_from_city_center
        return round(price1 * price2, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        else:
            return 0

    def rate_service(self, mark: int) -> None:
        count_of_marks = mark + self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(count_of_marks / self.count_of_ratings, 1)
