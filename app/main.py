class Car:
    def __init__(self,
                 comfort_class: float,
                 clean_mark: float,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: float,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def rate_service(self, rate: float) -> None:
        total_rating = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = (total_rating + rate) / self.count_of_ratings
        self.average_rating = round(self.average_rating, 1)

    def calculate_washing_price(self, car: Car) -> float:
        comfort_class = car.comfort_class
        clean_diff = self.clean_power - car.clean_mark
        rating = self.average_rating
        distance = self.distance_from_city_center
        return (comfort_class * clean_diff * rating) / distance

    def wash_single_car(self, cars: list[Car]) -> list[Car]:
        washed_cars = []
        for car in cars:
            if isinstance(car, Car) and self.clean_power >= car.clean_mark:
                washed_cars.append(car)
        return washed_cars

    def serve_cars(self, cars: list) -> float:
        washed_cars = self.wash_single_car(cars)
        total_price = 0.0
        for car in washed_cars:
            total_price += self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
        return round(total_price, 1)
