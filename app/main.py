class Car:
    def __car_info__(self, comfort_class: int, clean_mark: int,
                     brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __wash_station_info__(self, distance_from_city_center: float,
                              clean_power: int, average_rating: float,
                              count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car_cal: Car) -> float:
        price = car_cal.comfort_class
        price*= (self.clean_power - car_cal.clean_mark)
        price *= self.average_rating / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, dirty_car: Car) -> None:
        if dirty_car.clean_mark < self.clean_power:
            dirty_car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> int:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def rate_service(self, rate: int) -> None:
        new_average = (self.average_rating * self.count_of_ratings + rate)
        new_average /= (self.count_of_ratings + 1)
        self.count_of_ratings += 1
        self.average_rating = round(new_average, 1)
