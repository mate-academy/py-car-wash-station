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
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def should_car_be_washed(self, clean_mark: int) -> bool:
        return self.clean_power > clean_mark

    def calculate_washing_price(self, car: Car) -> float:
        return round((car.comfort_class * (self.clean_power - car.clean_mark)
                      * self.average_rating) / self.distance_from_city_center,
                     1)

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power

        return price

    def rate_service(self, mark: float) -> None:
        current_total_rate = self.average_rating * self.count_of_ratings
        current_total_rate += mark
        self.count_of_ratings += 1

        self.average_rating = round(current_total_rate / self
                                    .count_of_ratings, 1)

    def serve_cars(self, cars: [Car]) -> float:
        income = 0.0

        for car in cars:
            if self.should_car_be_washed(car.clean_mark):
                income += self.wash_single_car(car)

        return income
