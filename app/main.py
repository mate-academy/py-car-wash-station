class Car:
    def __init__(self, comfort_clas: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_clas
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, dist: int, power: int, rating: int, count: int) -> None:
        self.distance_from_city_center = dist
        self.clean_power = power
        self.average_rating = rating
        self.count_of_ratings = count

    def serve_cars(self, count_of_cars: list) -> int:
        income = 0
        for car in count_of_cars:
            if car.clean_mark <= self.clean_power:
                income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: classmethod) -> int:
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 2)

    def wash_single_car(self, car: classmethod) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        else:
            print("Sorry, but your car is clean enough!")

    def rate_service(self, rating_a_service: int) -> None:
        calc_of_rating = ((self.average_rating * self.count_of_ratings)
                          + rating_a_service) / (self.count_of_ratings + 1)
        self.average_rating = round(calc_of_rating, 1)
        self.count_of_ratings += 1
