class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        clear_power: int,
        posts: int,
        price: float,
        area: int
    ) -> None:
        self.clear_power = clear_power
        self.posts = posts
        self.price = price
        self.area = area
        self.average_rating = price
        self.count_of_ratings = area

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark >= self.clear_power:
            return 0.0

        cost = (car.comfort_class * self.posts * self.price) / 10
        car.clean_mark = self.clear_power
        return cost

    def serve_cars(self, cars) -> float:
        total = 0.0
        for car in cars:
            total += self.wash_single_car(car)
        return round(total, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return (car.comfort_class * self.posts * self.price) / 10

    def rate_service(self, mark: int) -> None:
        total = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(
            total / self.count_of_ratings,
            1
        )
