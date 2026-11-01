from collections.abc import Iterable, Iterator


class Car:
    def __init__(
        self,
        comfort_class: int,
        clean_mark: int,
        brand: str,
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

    def serve_cars(self, cars: Iterable[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)

    def __str__(self) -> str:
        return (
            "CarWashStation("
            f"distance_from_city_center={self.distance_from_city_center}, "
            f"clean_power={self.clean_power}, "
            f"average_rating={self.average_rating}, "
            f"count_of_ratings={self.count_of_ratings})"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CarWashStation):
            return NotImplemented
        return (
            self.distance_from_city_center == other.distance_from_city_center
            and self.clean_power == other.clean_power
            and self.average_rating == other.average_rating
            and self.count_of_ratings == other.count_of_ratings
        )

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, CarWashStation):
            return NotImplemented
        return self.average_rating < other.average_rating

    def __le__(self, other: object) -> bool:
        if not isinstance(other, CarWashStation):
            return NotImplemented
        return self.average_rating <= other.average_rating

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, CarWashStation):
            return NotImplemented
        return self.average_rating > other.average_rating

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, CarWashStation):
            return NotImplemented
        return self.average_rating >= other.average_rating

    def __hash__(self) -> int:
        return hash(
            (
                self.distance_from_city_center,
                self.clean_power,
                self.average_rating,
                self.count_of_ratings,
            )
        )

    def __copy__(self) -> "CarWashStation":
        return CarWashStation(
            self.distance_from_city_center,
            self.clean_power,
            self.average_rating,
            self.count_of_ratings,
        )

    def __deepcopy__(self, memo: dict[int, object]) -> "CarWashStation":
        return CarWashStation(
            self.distance_from_city_center,
            self.clean_power,
            self.average_rating,
            int(self.count_of_ratings),
        )

    def __bool__(self) -> bool:
        return (
            self.clean_power > 0
            and self.average_rating > 0
            and self.count_of_ratings > 0
        )

    def __len__(self) -> int:
        return int(self.count_of_ratings)

    def __getitem__(self, index: int) -> float | int:
        if index == 0:
            return self.distance_from_city_center
        if index == 1:
            return self.clean_power
        if index == 2:
            return self.average_rating
        if index == 3:
            return self.count_of_ratings
        raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: float | int) -> None:
        if index == 0:
            self.distance_from_city_center = float(value)
        elif index == 1:
            self.clean_power = int(value)
        elif index == 2:
            self.average_rating = float(value)
        elif index == 3:
            self.count_of_ratings = int(value)
        else:
            raise IndexError("Index out of range")

    def __delitem__(self, index: int) -> None:
        if index == 0:
            self.distance_from_city_center = 0
        elif index == 1:
            self.clean_power = 0
        elif index == 2:
            self.average_rating = 0
        elif index == 3:
            self.count_of_ratings = 0
        else:
            raise IndexError("Index out of range")

    def __contains__(self, item: object) -> bool:
        return item in (
            self.distance_from_city_center,
            self.clean_power,
            self.average_rating,
            self.count_of_ratings,
        )

    def __iter__(self) -> Iterator[float | int]:
        yield self.distance_from_city_center
        yield self.clean_power
        yield self.average_rating
        yield self.count_of_ratings

    def __reversed__(self) -> Iterator[float | int]:
        yield self.count_of_ratings
        yield self.average_rating
        yield self.clean_power
        yield self.distance_from_city_center

    def __call__(self, *args: float | int, **kwargs: object) -> None:
        if args:
            self.distance_from_city_center = args[0]
        if len(args) > 1:
            self.clean_power = int(args[1])
        if len(args) > 2:
            self.average_rating = args[2]
        if len(args) > 3:
            self.count_of_ratings = int(args[3])

    def __enter__(self) -> "CarWashStation":
        return self
