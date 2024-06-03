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

    def calculate_washing_price(self, car_to_wash: Car) -> float:
        sum_for_wash = (car_to_wash.comfort_class
                        * (self.clean_power - car_to_wash.clean_mark)
                        * self.average_rating / self.distance_from_city_center)
        return round(sum_for_wash, 1)

    def wash_single_car(self, car_to_wash: Car) -> None:
        if self.clean_power >= car_to_wash.clean_mark:
            car_to_wash.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

    def serve_cars(self, list_of_cars: list[Car]) -> int:
        total_sum = 0
        for car in list_of_cars:
            if self.clean_power >= car.clean_mark:
                total_sum += self.calculate_washing_price(car)
                self.wash_single_car(car)

        return total_sum
