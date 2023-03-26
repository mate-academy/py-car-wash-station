class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(
            self,
            cars
    ):
        total = 0
        for car in cars:
            if car.clean_mark <= self.clean_power:
                total += self.calculate_washing_price(car)
            self.wash_single_car(car)

        return round(total, 1)

    def calculate_washing_price(
            self,
            car
    ):
        result = car.comfort_class * (self.clean_power - car.clean_mark)
        result = result * self.average_rating / self.distance_from_city_center

        return round(result, 1)

    def wash_single_car(
            self,
            car
    ):
        if car.clean_mark > self.clean_power:
            return f"{car.brand} wasn't washed"
        car.clean_mark = self.clean_power

        return f"all other car are washed to {car.clean_mark}"

    def rate_service(
            self,
            rating
    ):
        average_rate = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        average_rate = (average_rate + rating) / self.count_of_ratings
        self.average_rating = round(average_rate, 1)

        return round(average_rate, 1)
