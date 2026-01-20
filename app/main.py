class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
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

    def serve_cars(self, car_pack: list) -> int | None:
        total_amount = 0
        for car in car_pack:
            if self.clean_power > car.clean_mark:
                print(
                    f"\nOur washing power {self.clean_power} - "
                    f"serving >{car.brand}<"
                    f" with {car.clean_mark} lvl clean mark"
                )
                total_amount += self.calculate_washing_price(car)
                self.wash_single_car(car)
            else:
                print(
                    f"\n{car.brand} - washing power - "
                    f"{car.clean_mark} NOT SUPPORTED THIS CarWashStation!"
                )
        print(f"\nTotal bill - {total_amount}$")
        return total_amount

    def calculate_washing_price(self, car: Car) -> float:
        return round(
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * (self.average_rating / self.distance_from_city_center),
            1,
        )

    def wash_single_car(self, car: Car) -> int:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        else:
            print(
                f"Cleaning power insufficient for {car.brand} "
                f"with clean mark "
                f"{car.clean_mark}. No changes made."
            )
        return car.clean_mark

    def rate_service(self, num: float) -> float:
        if self.count_of_ratings == 0:
            self.average_rating = round(num, 1)
            self.count_of_ratings = 1
        else:
            self.average_rating = round(
                (self.average_rating * self.count_of_ratings + num)
                / (self.count_of_ratings + 1),
                1,
            )
            self.count_of_ratings += 1
        print(f"Our new rating - {round(self.average_rating, 1)}")
        return self.average_rating
