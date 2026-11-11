from decimal import Decimal, ROUND_HALF_UP


def round_half_up(val: float, decimals: int = 1) -> float:
  """Rounds a float value using standard half-up rounding."""
  d = Decimal(str(val))
  return float(
      d.quantize(Decimal("1." + "0" * decimals), rounding=ROUND_HALF_UP)
  )


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
    price = (
        car.comfort_class
        * (self.clean_power - car.clean_mark)
        * self.average_rating
        / self.distance_from_city_center
    )
    return round_half_up(price, 1)

  def wash_single_car(self, car: Car) -> None:
    if self.clean_power > car.clean_mark:
      car.clean_mark = self.clean_power

  def serve_cars(self, cars: list[Car]) -> float:
    total_income = 0.0
    for car in cars:
      if car.clean_mark < self.clean_power:
        price = self.calculate_washing_price(car)
        total_income += price
        self.wash_single_car(car)
    return round_half_up(total_income, 1)

  def rate_service(self, rating: int) -> None:
    total_score = self.average_rating * self.count_of_ratings + rating
    self.count_of_ratings += 1
    self.average_rating = round_half_up(total_score / self.count_of_ratings, 1)