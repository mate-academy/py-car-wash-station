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

    def serve_cars(self, cars: list[Car]) -> float | int:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        result = (car.comfort_class
                  * (self.clean_power - car.clean_mark)
                  * (self.average_rating / self.distance_from_city_center))

        final_result = round(result, 1)

        return final_result

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> None:
        total_rating_sum = self.average_rating * self.count_of_ratings
        new_total_rating_sum = total_rating_sum + new_rating
        new_average_rating = new_total_rating_sum / (self.count_of_ratings + 1)

        self.average_rating = round(new_average_rating, 1)
        self.count_of_ratings += 1
