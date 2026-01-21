class Car:
    def __init__(self, model: str, is_clean: bool = False) -> None:
        self.model = model
        self.is_clean = is_clean

    def wash(self) -> None:
        self.is_clean = True


class CarWashStation:
    def __init__(self, workers: int, posts: int, price: float, area: int) -> None:
        self.workers = workers
        self.posts = posts
        self.price = price
        self.area = area
        self.cleaned_cars = 0

    def wash_car(self, car: Car) -> None:
        car.wash()
        self.cleaned_cars += 1
