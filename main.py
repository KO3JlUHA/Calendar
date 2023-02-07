# import pygame

months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
days_name = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months_codes = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]


class Date:
    def __init__(self, day_of_month: int, month: int, year: int, is_human_date: bool) -> None:
        self.day_of_month = day_of_month - is_human_date
        self.month = month - is_human_date
        self.year = year
        self.day_of_week = self.get_day_of_week_as_string()
        self.notes = []

    def __repr__(self) -> str:
        s = f'{self.day_of_week[:3]} '
        s += f'{self.day_of_month + 1}'.zfill(2)
        s += '/'
        s += f'{self.month + 1}'.zfill(2)
        s += f'/{self.year}'
        return s

    def get_day_of_week_by_date(self) -> int:
        return ((self.year % 100 + self.year % 100 // 4) % 7 + months_codes[
            self.month] + self.day_of_month - is_leap_year(year=self.year) * int(self.month < 2)) % 7

    def get_day_of_week_as_string(self) -> str:
        return days_name[self.get_day_of_week_by_date()]

    def get_notes(self) -> list:
        return self.notes

    def add_note(self, note) -> None:
        self.notes.append(note)


class Note:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        if self.description:
            return f'{self.name}\n{self.description}'
        return f'{self.name}'


def is_leap_year(year: int) -> bool:
    return (not year % 4) and bool(year % 100)


def string_to_date(date: str) -> Date:
    day, month, year = str(date).split('/')
    return Date(day_of_month=day, month=month, year=year, is_human_date=True)


def generate_year_array(year: int) -> list:
    year_array = []
    for month in range(12):
        year_array.append(generate_month_array(month=month, year=year))
    return year_array


def print_year(year: int) -> None:
    year_obj = generate_year_array(year=year)
    for month in year_obj:
        print_month(month=year_obj.index(month), year=year)
        print()


def generate_month_array(month: int, year: int) -> list:
    month_array = []
    months_length[1] += is_leap_year(year)
    for day in range(months_length[month]):
        month_array.append(Date(day_of_month=day, month=month, year=year, is_human_date=False))
    months_length[1] = 28
    return month_array


def print_month(month: int, year: int) -> None:
    month_obj = generate_month_array(month=month, year=year)
    start_day = month_obj[0].get_day_of_week_by_date()
    print(months_name[month], year)
    print('+----+----+----+----+----+----+----+')
    print('|SUN |MON |TUE |WED |THU |FRI |SAT |')
    for weeks in range(6):
        s1 = '+'
        s2 = '|'
        for days in range(7):
            s1 += '----+'
            if not len(month_obj) > 7 * weeks + days - start_day >= 0:
                s2 += '    |'
            else:
                x = f'{month_obj[7 * weeks + days - start_day].day_of_month + 1}'.zfill(2)
                if x.startswith('0'):
                    x = x.replace('0', ' ')
                s2 += f' {x} |'
        if s2 != '|    |    |    |    |    |    |    |':
            print(s1)
            print(s2)
    print('+----+----+----+----+----+----+----+')


def main() -> None:
    print_month(month=1, year=2004)


if __name__ == '__main__':
    main()
