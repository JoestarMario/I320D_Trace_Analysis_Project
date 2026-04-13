class Date():

    def __init__(self, date: str) -> None:
        places: list[str] = date.split('-')
        self.year: int = int(places[0])
        self.month: int = int(places[1])
        self.day: int = int(places[2])

    def __gt__(self, other) -> bool:
        if self.year != other.year:
            return self.year > other.year
        elif self.month != other.month:
            return self.month > other.month
        else:
            return self.day > other.day
    

    def __eq__(self, other) -> bool:
        return (self.year == other.year) and (self.month == other.month) and (self.day == other.day)



    def __str__(self) -> str:

        places: list[str] = []

        for place in [self.year, self.month, self.day]:
            if place < 10:
                places.append("0" + str(place))
            else:
                places.append(str(place))

        return "-".join(places)

    
    def __repr__(self) -> str:
        return str(self)
    

def main() -> None:
    d: Date = Date("2021-03-17")
    d2: Date = Date("2022-09-13")
    print(d == d2)


if __name__ == '__main__':
    main()