class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand
        if comfort_class > 7 or comfort_class < 1:
            raise ValueError("invalid car class value: it must be from 1 to 7")
        if clean_mark > 10 or clean_mark < 1:
            raise ValueError("invalid clean_mark: it must be from 1 to 10")


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings
        if distance_from_city_center < 1.0 or distance_from_city_center > 10.0:
            raise ValueError("invalid distance from city center:"
                             " it must be from 1.0 to 10.0")
        if average_rating < 1.0 or average_rating > 5.0:
            raise ValueError("invalid average_rating:"
                             " it must be from 1.0 to 5.0")

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_rating + rating)
                                    / self.count_of_ratings, 1)
