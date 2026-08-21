
def check_number(assigned_number: int | float,
                 left_border: int | float,
                 right_border: int | float) -> int | float:
    if left_border <= assigned_number <= right_border:
        number = assigned_number
    elif assigned_number < left_border:
        number = left_border
    else:
        number = right_border
    return number


class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = check_number(comfort_class, 1, 7)
        self.clean_mark = check_number(clean_mark, 1, 10)
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = check_number(
            distance_from_city_center, 1.0, 10.0)
        self.clean_power = check_number(clean_power, 1, 10)
        self.average_rating = check_number(average_rating,
                                           1.0,
                                           5.0)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, washed_car: Car) -> float:
        return round((washed_car.comfort_class
                      * (self.clean_power - washed_car.clean_mark)
                      * self.average_rating
                      / self.distance_from_city_center), 1)

    def rate_service(self, rate: float) -> None:
        rates_sum = self.average_rating * self.count_of_ratings
        rates_sum += round(rate, 1)
        self.count_of_ratings += 1
        self.average_rating = round(rates_sum / self.count_of_ratings, 1)

    def wash_single_car(self, car: Car) -> float:
        income = 0
        if car.clean_mark < self.clean_power:
            income = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return round(income, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            income += self.wash_single_car(car)
        return income
