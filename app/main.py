class Car:
    def __init__(self,
                 comfort_class: float,
                 clean_mark: float,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: float, average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
        self.rating_list = [average_rating for i in range(count_of_ratings)]

    def serve_cars(
            self,
            car_list: [Car]
    ) -> float:
        total_cost = 0
        for car in car_list:
            wash_cost = self.calculate_washing_price(car)
            if self.wash_single_car(car):
                total_cost += wash_cost
        return total_cost

    def calculate_washing_price(
            self,
            car: Car
    ) -> float:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * (self.average_rating / self.distance_from_city_center),
                     1)

    def wash_single_car(self, car: Car) -> bool:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power
            return True
        return False

    def rate_service(self, rate: float) -> None:
        self.rating_list.append(rate)
        self.count_of_ratings = len(self.rating_list)
        self.average_rating = round(sum(self.rating_list)
                                    / self.count_of_ratings, 1)
