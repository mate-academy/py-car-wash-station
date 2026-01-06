class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("Comfort class must be between 1 and 7")
        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("Clean mark must be between 1 and 10")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        if distance_from_city_center < 1.0 or distance_from_city_center > 10.0:
            raise ValueError(
                "Distance from city center"
                " must be between 1.0 and 10.0"
            )
        if average_rating < 1.0 or average_rating > 5.0:
            raise ValueError("Average rating must be between 1.0 and 5.0")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        return sum(self.wash_single_car(car) for car in cars)

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark > self.clean_power:
            return 0

        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center
            , 1)

    def rate_service(self, mark: int) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + mark)
            / (self.count_of_ratings + 1)
            , 1)
        self.count_of_ratings += 1
