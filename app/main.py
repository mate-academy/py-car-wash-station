class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: int,
            clean_power: int,
            average_rating: int,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        washing_amount = 0
        for car in cars:
            if car.clean_mark > self.clean_power:
                break
            else:
                washing_amount += self.wash_single_car(car)
                car.clean_mark = self.clean_power

        return washing_amount

    def calculate_washing_price(self, cars: list[Car]) -> float:
        cost_of_washing = 0
        for car in cars:
            if car.clean_mark > self.clean_power:
                break
            else:
                cost_of_washing += self.wash_single_car(car)

        return cost_of_washing

    def wash_single_car(self, car: Car) -> float:
        cost_of_washing = (
                car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center
        )

        return round(cost_of_washing, 1)

    def rate_service(self, response: int) -> None:
        new_rating = (
                (self.average_rating * self.count_of_ratings + response)
                / (self.count_of_ratings + 1)
        )
        self.average_rating = round(new_rating, 1)
        self.count_of_ratings += 1
