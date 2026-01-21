class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for vehicle in cars:
            if self.clean_power >= vehicle.clean_mark:
                income += self.calculate_washing_price(vehicle)
                self.wash_single_car(vehicle)
        return round(income, 1)

    def calculate_washing_price(self, vehicle: Car) -> float:
        price = (vehicle.comfort_class * (self.clean_power - vehicle.clean_mark)
                 * (self.average_rating / self.distance_from_city_center))
        return round(price, 1)

    def wash_single_car(self, vehicle: Car) -> None:

        vehicle.clean_mark = self.clean_power

    def rate_service(self, single_rating: float) -> None:
        overall_rating = self.count_of_ratings * self.average_rating
        self.count_of_ratings += 1
        self.average_rating = round(((overall_rating + single_rating)
                               / self.count_of_ratings),1)
