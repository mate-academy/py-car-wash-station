class CarWashStation:
    def __init__(self) -> None:
        self.cars_washed: int = 0

    def wash(self, car_qty: int) -> None:
        self.cars_washed += car_qty

    def status(self) -> str:
        return f"Мийка обробила {self.cars_washed} машин."
