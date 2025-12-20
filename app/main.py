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

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                price = self.calculate_washing_price(car)
                income += price
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        max_difference = max(self.clean_power, car.clean_mark)
        min_difference = min(self.clean_power, car.clean_mark)
        clean_difference = max_difference - min_difference
        comfort = car.comfort_class
        avg_rating = self.average_rating
        car_clean_average = comfort * clean_difference * avg_rating
        price = car_clean_average / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        self.count_of_ratings += 1
        old_avg = self.average_rating
        rating_count = self.count_of_ratings
        new_average = old_avg + (rating - old_avg) / rating_count
        self.average_rating = round(new_average, 1)
