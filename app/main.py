class Car:
    def __init__(self, comfort_class : int,
                 clean_mark : int, brand : str) -> None:
        if comfort_class < 8 and comfort_class > 0 :
            self.comfort_class = comfort_class
        if clean_mark < 11 and clean_mark > 0:
            self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center : float,
                 clean_power : int, average_rating : float,
                 count_of_ratings : int) -> None:
        if (distance_from_city_center < 10.1
                and distance_from_city_center > 0.9):
            self.distance_from_city_center = distance_from_city_center
        if clean_power < 11 and clean_power > 0:
            self.clean_power = clean_power
        if average_rating < 5.1 and average_rating > 0.9:
            self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def wash_single_car(self, car : Car) -> None:
        if (car.clean_mark < self.clean_power):
            car.clean_mark = self.clean_power

    def serve_cars(self, cars : list[Car]) -> float:
        result = []
        for car in cars:
            if (car.clean_mark < self.clean_power):
                result.append(
                    CarWashStation.calculate_washing_price(self, car))
                CarWashStation.wash_single_car(self, car)
        return round(sum(result), 1)

    def calculate_washing_price(self, car : Car) -> float:
        return round((car.comfort_class * (self.clean_power
                      - car.clean_mark) * self.average_rating
                      / self.distance_from_city_center), 1)

    def rate_service(self, rate : int) -> None:
        self.count_of_ratings += 1
        self.average_rating = (((self.average_rating
                                 * (self.count_of_ratings - 1)) + rate)
                               / self.count_of_ratings)
        self.average_rating = round(self.average_rating, 1)
