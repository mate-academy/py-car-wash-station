class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        self.comfort_class = max(1, min(7, comfort_class))
        self.clean_mark = max(1, min(10, clean_mark))
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = max(
            1.0, min(10.0, distance_from_city_center))
        self.clean_power = clean_power
        self.average_rating = round(max(1.0, min(5.0, average_rating)), 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> list:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                cost = (car.comfort_class * (self.clean_power - car.clean_mark)
                        * (self.average_rating
                           / self.distance_from_city_center))

                income += cost  # 🔥 Najpierw dodajemy koszt, a potem myjemy
                #
                # print(f"🚗 Washing {car.brand} | Clean_mark: {car.clean_mark}
                # -> {self.clean_power} | Cost: {cost}")
                # print(f"💰 Current Income: {income}")

                self.wash_single_car(car)  # 🚀 Teraz myjemy auto

        print(f"💰 Total Income: {income}")  # 🔥 Final debug
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        if car.clean_mark < self.clean_power:
            cost = (car.comfort_class * (self.clean_power - car.clean_mark)
                    * (self.average_rating / self.distance_from_city_center))
            return round(cost, 1)
        return 0.0

    def wash_single_car(self, car: Car) -> Car:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating: float) -> float:
        new_rating = round(max(1.0, min(5.0, new_rating)), 1)
        self.count_of_ratings += 1
        self.average_rating = round(
            ((self.average_rating * (self.count_of_ratings - 1))
             + new_rating) / self.count_of_ratings, 1
        )  # ✅ Poprawka do średniej oceny
