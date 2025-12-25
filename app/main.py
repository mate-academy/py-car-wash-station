from typing import List, Dict, Any


class Car:
    def __init__(
        self,
        comfort_class: str,
        clean_mark: float,
        brand: str
    ) -> None:
        self.comfort_class = comfort_class.lower()
        self.clean_mark = float(clean_mark)
        self.brand = brand

    def __repr__(self) -> str:
        return (
            f"Car({self.brand}, "
            f"{self.comfort_class}, "
            f"{self.clean_mark})"
        )


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: float,
        average_rating: float = 0.0,
        count_of_ratings: int = 0
    ) -> None:
        self.distance_from_city_center = float(distance_from_city_center)
        self.clean_power = float(clean_power)
        self.average_rating = float(average_rating)
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        base_map = {
            "economy": 50.0,
            "standard": 75.0,
            "comfort": 100.0,
            "business": 150.0,
            "premium": 200.0,
        }

        base = base_map.get(car.comfort_class, 80.0)
        dirtiness = max(0.0, (10.0 - car.clean_mark) / 10.0)
        multiplier = 1.0 + dirtiness
        distance = 0.5 * self.distance_from_city_center
        discount = max(
            0.0,
            min(0.20, (self.clean_power - 50.0) / 250.0)
        )

        price = base * multiplier * (1 - discount) + distance
        return round(price, 2)

    def wash_single_car(self, car: Car) -> float:
        price = self.calculate_washing_price(car)
        car.clean_mark = 10.0
        return price

    def serve_cars(self, cars: List[Car]) -> Dict[str, Any]:
        details = []
        total = 0.0

        for car in cars:
            price = self.wash_single_car(car)
            details.append(
                {
                    "brand": car.brand,
                    "comfort_class": car.comfort_class,
                    "price": price,
                }
            )
            total += price

        return {
            "total_cars": len(details),
            "total_income": round(total, 2),
            "details": details,
        }

    def rate_service(self, new_rating: float) -> float:
        total_score = self.average_rating * self.count_of_ratings
        total_score += float(new_rating)
        self.count_of_ratings += 1
        self.average_rating = round(
            total_score / self.count_of_ratings,
            2
        )
        return self.average_rating
