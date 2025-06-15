from station import CarWashStation


def main() -> None:
    station = CarWashStation()
    station.wash(5)
    station.wash(3)
    print(station.status())  # Очікувано: Мийка обробила 8 машин.

if __name__ == "__main__":
    main()
