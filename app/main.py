class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: int):
        count = 0

        for car in cars:
            if car.clean_mark < self.clean_power:
                count += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(count, 1)

    def calculate_washing_price(self, cars: int):
        calculate = cars.comfort_class * (self.clean_power - cars.clean_mark)
        return round(
            calculate * self.average_rating / self.distance_from_city_center, 1
        )

    def wash_single_car(self, cars: int):
        if cars.clean_mark < self.clean_power:
            cars.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        ratings = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        up_ratings = round((ratings / self.count_of_ratings), 1)
        self.average_rating = up_ratings
        return self.average_rating
