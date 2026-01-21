class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:

        if comfort_class < 1 or comfort_class > 7:
            raise ValueError("comfort_class має бути від 1 до 7")
        if clean_mark < 1 or clean_mark > 10:
            raise ValueError("clean_mark має бути від 1 до 10")
        # визначення атрибутів
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float,
                 count_of_ratings: int) -> None:
        if distance_from_city_center < 1.0 or distance_from_city_center > 10.0:
            raise ValueError("distance_from_city_center має бути від 1.0 до 10.0.")
        if clean_power < 1 or clean_power > 10:
            raise ValueError("clean_power має бути від 1 до 10.")
        if average_rating < 1.0 or average_rating > 5.0:
            raise ValueError("average_rating має бути від 1.0 до 5.0.")
        if count_of_ratings < 0:
            raise ValueError("count_of_ratings має бути не від'ємним.")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        washing_price = (car.comfort_class *
                         (self.clean_power - car.clean_mark) *
                         self.average_rating / self.distance_from_city_center)
        return round(washing_price, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_price = self.calculate_washing_price(car)
                total_income += wash_price
                self.wash_single_car(car)

        return round(total_income, 1)

    def rate_service(self, new_rating: int) -> None:
        if new_rating < 1 or new_rating > 5:
            raise ValueError("Рейтинг має бути від 1 до 5.")

        total_rating = (self.average_rating * self.count_of_ratings) + new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)
