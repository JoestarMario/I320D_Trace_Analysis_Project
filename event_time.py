class Time():
    def __init__(self, time: str) -> None:
        time: str = time.split('-')[0]

        places: list[str] = time.split(':')

        self.hour: int = int(places[0])
        self.minute: int = int(places[1])
        self.second: int = int(places[2])


    def __float__(self) -> float:

        float_hour: float = float(self.hour)
        float_minute: float = (float(self.minute) / 60)
        float_second: float = (float(self.second) / (60**2))

        return float_hour + float_minute + float_second


    def __gt__(self, other) -> bool:
        return float(self) > float(other)
    
    
    def __eq__(self, other) -> bool:
        return float(self) == float(other)
    

    def __str__(self) -> str:

        places: list[str] = []

        for place in [self.hour, self.minute, self.second]:
            if place < 10:
                places.append("0" + str(place))
            else:
                places.append(str(place))

        return ":".join(places)

    
    def __repr__(self) -> str:
        return str(self)


def main() -> None:
    t: Time = Time('6:5:44')
    print(float(t))


if __name__ == '__main__':
    main()