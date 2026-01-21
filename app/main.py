class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        count = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                count += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(count, 1)

    def calculate_washing_price(self, car: Car) -> float:
        washing_effort = self.clean_power - car.clean_mark
        washing_rating = self.average_rating / self.distance_from_city_center
        return round(car.comfort_class * washing_effort * washing_rating, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, stars: int) -> None:
        marks = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((stars + marks) / self.count_of_ratings, 1)
