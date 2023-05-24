class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        return sum(self.wash_single_car(car) for car in cars)

    def calculate_washing_price(self, car: Car) -> float:
        cleaning = self.clean_power - car.clean_mark
        comfort_by_cleaning = car.comfort_class * cleaning
        final_product = comfort_by_cleaning * self.average_rating
        return round(final_product / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0

    def rate_service(self, rating: int) -> None:
        sum_of_ratings = self.average_rating * self.count_of_ratings
        new_sum = sum_of_ratings + rating
        self.average_rating = round(new_sum / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
