class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for i in cars:
            if i.clean_mark < self.clean_power:
                income += self.calculate_washing_price(i)
                self.wash_single_car(i)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        profit = round((car.comfort_class * (self.clean_power - car.clean_mark)
                        * self.average_rating
                        / self.distance_from_city_center), 1)
        return profit

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, number: int) -> None:
        all_marks = self.average_rating * self.count_of_ratings + number
        self.count_of_ratings += 1
        average_rate = all_marks / self.count_of_ratings
        self.average_rating = round(average_rate, 1)
