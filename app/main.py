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
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list[Car]) -> float:
        total_price = 0
        for car in car_list:
            total_price += self.wash_single_car(car)
        return total_price

    def calculate_washing_price(self, car: Car) -> float:
        wash_progress = 0
        if self.clean_power - car.clean_mark > 0:
            wash_progress = self.clean_power - car.clean_mark
        wash_price = (
            (car.comfort_class * wash_progress * self.average_rating)
            / self.distance_from_city_center)
        return round(wash_price, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        else:
            return 0

    def rate_service(self, rate: int) -> None:
        if rate < 1 or rate > 5:
            raise ValueError("Rate must be between 1 and 5")
        else:
            new_rate_sum = self.average_rating * self.count_of_ratings + rate
            new_rate_count = self.count_of_ratings + 1
            self.average_rating = round(new_rate_sum / new_rate_count, 1)
            self.count_of_ratings += 1
