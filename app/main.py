class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        return round(car.comfort_class * (self.clean_power - car.clean_mark)
                     * self.average_rating / self.distance_from_city_center, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list):
        income_state = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income_state += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return income_state

    def rate_service(self, rate: int):
        if rate in range(1, 6):
            self.average_rating = round((self.average_rating * self.count_of_ratings + rate)
                                        / (self.count_of_ratings + 1), 1)
            self.count_of_ratings += 1
