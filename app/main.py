class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        diff = int(self.clean_power) - int(car.clean_mark)
        comfort = int(car.comfort_class)
        rating = float(self.average_rating)
        price = comfort * diff * rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        if rating in range(1, 6):
            new_count = self.count_of_ratings + 1
            old_rating = self.average_rating
            old_count = self.count_of_ratings
            self.average_rating = (old_rating * old_count + rating) / new_count
            self.average_rating = round(self.average_rating, 1)
            self.count_of_ratings = new_count

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if self.clean_power > car.clean_mark:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)
