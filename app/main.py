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
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> None:
        cost = car.comfort_class
        cleanwas = car.clean_mark
        cleanis = self.clean_power
        effect = cleanis - cleanwas
        cost *= effect
        cost *= self.average_rating
        cost /= self.distance_from_city_center
        cost = round(cost + 0.001, 1)
        return cost

    def rate_service(self, single_rate: int) -> None:
        old_rate = self.average_rating
        new_count_of_ratings = self.count_of_ratings + 1
        new_rate = ((old_rate * self.count_of_ratings + single_rate)
                    / (new_count_of_ratings))
        self.count_of_ratings = new_count_of_ratings
        self.average_rating = round(new_rate, 1)

    def wash_single_car(self, car: Car) -> float:
        clean_mark_car = car.clean_mark
        if clean_mark_car >= self.clean_power:
            return 0
        result = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return result

    def serve_cars(self, cars: list) -> float:
        result = 0
        for car in cars:
            oneincome = self.wash_single_car(car)
            result += oneincome
        return result
