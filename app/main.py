class Car:
    def __init__(self, comfort_class: int,
                 clean_mark: int, brand: str) -> None:
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            raise ValueError("Error. comfort_class must be between 1 and 7.")

        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            raise ValueError("Error. clean_mark must be between 1 and 10.")

        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_pover: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        else:
            raise ValueError("Error. distance_from_city_center must be "
                             "between 1.0 and 10.0.")

        if 1 <= clean_pover <= 10:
            self.clean_pover = clean_pover
        else:
            raise ValueError("Error. clean_pover must be between 1 and 10.")

        if 1.0 <= average_rating <= 5.0:
            self.average_rating = round(average_rating, 1)
        else:
            raise ValueError("Error. average_rating must "
                             "be between 1.0 and 5.0.")

        if not isinstance(count_of_ratings, int) or count_of_ratings < 0:
            raise ValueError("Error. count_of_ratings must be "
                             "a non-negative integer.")
        else:
            self.count_of_ratings = count_of_ratings

    def serve_car(self, cars: list) -> float:
        income = 0.0
        for car in cars:
            if (car.clean_mark
                    < self.clean_pover):
                wash_cost = self.calculate_washing_price(car)
                income += wash_cost  # Додати вартість до доходу
                self.wash_single_car(car)  # Оновити clean_mark машини
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return (car.comfort_class * (self.clean_pover - car.clean_mark)
                * self.average_rating / self.distance_from_city_center)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_pover > car.clean_mark:
            car.clean_mark = self.clean_pover

    def rate_service(self, new_rating: float) -> None:
        if 1.0 <= new_rating <= 5.0:
            total_rating = self.average_rating * self.count_of_ratings
            total_rating += new_rating
            self.count_of_ratings += 1
            self.average_rating = round(total_rating
                                        / self.count_of_ratings, 1)
        else:
            raise ValueError("Error. Rating must be between 1.0 and 5.0.")
