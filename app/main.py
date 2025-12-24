class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_of_car: list[Car]) -> float:
        price = 0
        for car in list_of_car:
            price_of_car = self.wash_single_car(car)

            if price_of_car is not None:
                price += price_of_car

        return round(price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        cost = (car.comfort_class * (
            self.clean_power - car.clean_mark)
            * self.average_rating / self.distance_from_city_center)
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> float | None:
        if car.clean_mark >= self.clean_power:
            return
        cost = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return cost

    def rate_service(self, rate: int) -> None:

        rating = self.count_of_ratings * self.average_rating + rate
        self.count_of_ratings += 1
        self.average_rating = round(rating / self.count_of_ratings, 1)

        return
