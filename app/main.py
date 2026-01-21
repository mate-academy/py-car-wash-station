class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        sum_washed_cars = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                calc = self.calculate_washing_price(car)
                sum_washed_cars += calc
                self.wash_single_car(car)

        sum_washed_cars_round = round(sum_washed_cars, 1)
        return sum_washed_cars_round

    def calculate_washing_price(self, car: Car) -> float:
        calc = (car.comfort_class * (self.clean_power - car.clean_mark)
                * self.average_rating / self.distance_from_city_center)
        result = round(calc, 1)
        return result

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, score: int) -> None:
        new_count = self.count_of_ratings + 1
        new_average = ((self.average_rating * self.count_of_ratings + score)
                       / new_count)
        round_new_avarage = round(new_average, 1)

        self.count_of_ratings = new_count
        self.average_rating = round_new_avarage
