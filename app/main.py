class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

    def __repr__(self) -> str:
        return (f"Car(brand={self.brand}, "
                f"clean_mark={self.clean_mark}, "
                f"comfort_class={self.comfort_class})")


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")
mercedes = Car(comfort_class=7, clean_mark=5, brand="Mercedes")


class CarWashStation:
    def __init__(self, distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            income_from_car = self.wash_single_car(car)
            print(f"Washing {car.brand}: income = {income_from_car}")
            total_income += income_from_car

        total_income = round(total_income, 1)
        print(f"Total income: {total_income}")
        return total_income

    def wash_single_car(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            washing_price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return washing_price
        return 0.0

    def calculate_washing_price(self, car: Car) -> float:
        calculated_washing_price = (
            car.comfort_class * (
                (self.clean_power - car.clean_mark)
                * (self.average_rating / self.distance_from_city_center)))
        return calculated_washing_price

    def rate_service(self, rating: float) -> None:
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + rating)
            / (self.count_of_ratings + 1), 1
        )
        self.count_of_ratings += 1
