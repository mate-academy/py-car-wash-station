class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, workers: int, posts: int, price: float, area: int
    ) -> None:
        self.workers = workers
        self.posts = posts
        self.price = price
        self.area = area
        self.clear_power = 7
        self.cleaned_cars = 0
        self.average_rating = price
        self.count_of_ratings = area

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark >= self.clear_power:
            return 0.0
        car.clean_mark = max(car.clean_mark, self.clear_power)
        self.cleaned_cars += 1
        return round(car.comfort_class * self.price * self.posts, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        total = 0.0
        for car in cars:
            total += self.wash_single_car(car)
        return round(total, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class * self.price * self.posts, 1)

    def rate_service(self, mark: int) -> None:
        total = self.average_rating * self.count_of_ratings + mark
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)
        
