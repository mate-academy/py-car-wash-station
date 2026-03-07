class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        # Almacena la clase de confort (1-7), nivel de limpieza (1-10) y marca
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(
        self, 
        distance_from_city_center: float, 
        clean_power: int, 
        average_rating: float, 
        count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calcula el precio: (clase * (poder - limpieza) * rating) / distancia.
        """
        diff = self.clean_power - car.clean_mark
        price = (car.comfort_class * diff * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """Actualiza la limpieza del coche si el poder de la estación es mayor."""
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list) -> float:
        """Lava una lista de coches y devuelve el ingreso total acumulado."""
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                # Calculamos el precio antes de lavar (para tener la diferencia real)
                total_income += self.calculate_washing_price(car)
                # Aplicamos el lavado
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rate: int) -> None:
        """Actualiza el promedio y el contador de calificaciones."""
        total_score = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_score + new_rate) / self.count_of_ratings, 1)
