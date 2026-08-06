class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if not 1 <= comfort_class <= 7:
            raise ValueError("comfort class of a car, from 1 to 7")
        self.comfort_class = comfort_class
        if not 1 <= clean_mark <= 10:
            raise (ValueError
                   ("car cleanness mark, from very dirty -"
                    "1 to absolutely clean - 10"))
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        if not 1.0 <= distance_from_city_center <= 10.0:
            raise ValueError("how far station from the city center, "
                             "from 1.0 to 10.0")
        self.distance_from_city_center = distance_from_city_center
        if not 1 <= clean_power <= 10:
            raise ValueError("clean power of station, from 1 to 10")
        self.clean_power = clean_power
        if not 1.0 <= average_rating <= 5.0:
            raise ValueError("average rating of the station, from 1.0 to 5.0")
        self.average_rating = round(average_rating, 1)
        if count_of_ratings < 0:
            raise ValueError("count_of_ratings must positive")
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: str) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating
                 / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: str) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def single_rate(self, rate: float) -> None:
        total_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round(((total_rate + rate)
                                     / self.count_of_ratings), 1)

    def rate_service(self, rate: float) -> None:
        self.single_rate(rate)
