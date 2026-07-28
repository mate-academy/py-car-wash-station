class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


bmw = Car(3, 3, "BMW")
audi = Car(4, 5, "Audi")


class CarWashStation:
    def __init__(
            self, distance_from_city_center: int | float,
            clean_power: int | float,
            average_rating: int | float,
            count_of_ratings: int | float) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> int | float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> int | float:
        total_price = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result = self.calculate_washing_price(car)
                total_price += result
                self.wash_single_car(car)
        return total_price

    def rate_service(self, new_rating: int) -> int | float:
        result = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        result += new_rating
        new_average_rating = result / self.count_of_ratings
        self.average_rating = round(new_average_rating, 1)
        return round(new_average_rating, 1)


car_wash_station = CarWashStation(5, 6, 3.5, 6)
