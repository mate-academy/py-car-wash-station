from typing import List


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
    ) -> None:
        if not (1 <= comfort_class <= 7):
            raise ValueError("comfort_class must be between 1 and 7")
        if not (1 <= clean_mark <= 10):
            raise ValueError("clean_mark must be between 1 and 10")

        self.comfort_class: int = comfort_class
        self.clean_mark: int = clean_mark
        self.brand: str = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("distance must be between 1.0 and 10.0")
        if not (1 <= clean_power <= 10):
            raise ValueError("clean_power must be between 1 and 10")
        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("average_rating must be between 1.0 and 5.0")
        if count_of_ratings < 0:
            raise ValueError("count_of_ratings cannot be negative")

        self.distance_from_city_center: float = distance_from_city_center
        self.clean_power: int = clean_power
        self.average_rating: float = round(average_rating, 1)
        self.count_of_ratings: int = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """Розрахунок вартості миття одного автомобіля"""
        diff = self.clean_power - car.clean_mark
        numerator = car.comfort_class * diff * self.average_rating
        price = numerator / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Миття одного автомобіля до clean_power"""
        if car.clean_mark < self.clean_power:
            car.clean_mark = min(self.clean_power, 10)

    def serve_cars(self, cars: List[Car]) -> float:
        """Обслуговування списку автомобілів і повернення доходу"""
        total_income: float = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, rating: int) -> None:
        """Додає рейтинг до станції та оновлює середній рейтинг"""
        total_rating: float = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


if __name__ == "__main__":
    # Демонстраційний код для тестування
    bmw = Car(3, 3, "BMW")
    audi = Car(4, 9, "Audi")
    mercedes = Car(7, 1, "Mercedes")

    ws = CarWashStation(6, 8, 3.9, 11)

    income = ws.serve_cars([bmw, audi, mercedes])
    print(income)               # 41.7
    print(bmw.clean_mark)       # 8
    print(audi.clean_mark)      # 9
    print(mercedes.clean_mark)  # 8

    ford = Car(2, 1, "Ford")
    wash_cost = ws.calculate_washing_price(ford)
    print(wash_cost)            # 9.1
    print(ford.clean_mark)      # 1  (не мито)

    ws.rate_service(5)
    print(ws.count_of_ratings)  # 12
    print(ws.average_rating)    # 4.0
