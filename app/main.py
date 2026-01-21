class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    
    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark >= self.clean_power:
            return 0.0

        washing_price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            washing_price = self.calculate_washing_price(car)
            if washing_price > 0:
                income += washing_price
                self.wash_single_car(car)
        return round(income, 1)

    def rate_service(self, rating: int) -> None:
        total_rating = self.average_rating * self.count_of_ratings + rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

def main() -> None:
    bmw = Car(3, 3, "BMW")
    audi = Car(4, 9, "Audi")
    mercedes = Car(7, 1, "Mercedes")
    wash_station = CarWashStation(6, 8, 3.9, 11)
    income = wash_station.serve_cars([bmw, audi, mercedes])
    print(income)
    print(bmw.clean_mark)
    print(audi.clean_mark)
    print(mercedes.clean_mark)

    ford = Car(2, 1, "Ford")
    wash_cost = wash_station.calculate_washing_price(ford)
    print(wash_cost)
    print(ford.clean_mark)
    wash_station.rate_service(5)
    print(wash_station.count_of_ratings)
    print(wash_station.average_rating)

if __name__ == "__main__":
    main()
