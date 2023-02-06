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

    def serve_cars(self, list_of_cars: list) -> float:
        total_sum = 0
        for car in list_of_cars:
            if car.clean_mark < self.clean_power:
                total_sum += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return total_sum

    def calculate_washing_price(self, car: Car) -> float:
        cost = round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center), 1)

        return cost

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        temp_rate = (self.average_rating * self.count_of_ratings) + rate
        self.count_of_ratings += 1
        self.average_rating = round(temp_rate / self.count_of_ratings, 1)
