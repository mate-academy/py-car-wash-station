class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: int,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: str) -> float:
        single_car_wash_price = (car.comfort_class
                                 * (self.clean_power - car.clean_mark)
                                 * (self.average_rating
                                    / self.distance_from_city_center))
        return round(single_car_wash_price, 1)

    def wash_single_car(self, car: str) -> int:
        if self.clean_power >= car.clean_mark:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def serve_cars(self, cars: list) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rate: int) -> None:
        sum_of_new_rating = self.average_rating * self.count_of_ratings + rate
        new_count_of_ratings = self.count_of_ratings + 1
        self.count_of_ratings = new_count_of_ratings
        self.average_rating = round(sum_of_new_rating
                                    / new_count_of_ratings, 1)
