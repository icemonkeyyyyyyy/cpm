from typing import List, Union


day_names = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница"
}


class Lesson:
    def __init__(self, lesson_name: str, cabinet: int):
        self.name = lesson_name
        self.cabinet = cabinet

    def get_name(self):
        return self.name

    def get_lesson(self):
        return [self.name, self.cabinet]


class Day:
    def __init__(self, lesson_names: List[str], cabinets: Union[List[int], range], day_number: int):
        self.day_number = day_number
        self.day_lessons = [Lesson(lesson_name=name, cabinet=cabinet) for name, cabinet in zip(lesson_names, cabinets)]


class Schedule:
    def __init__(self, days: list):
        self.days = [Day(lesson_names=day, cabinets=range(1, len(day) + 1), day_number=i + 1) for i, day in enumerate(days)]
        self.current_day = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_day < len(self.days):
            current_day = self.days[self.current_day]
            self.current_day += 1
            return current_day
        else:
            raise StopIteration

    def get_schedule(self):
        out_text = "Расписание:\n\n\n"
        for day in self.days:
            out_text += f"{day_names[day.day_number]}:\n\n"
            for lesson in day.day_lessons:
                out_text += f"Название: {lesson.get_lesson()[0]}\n" \
                            f"Кабинет: {lesson.get_lesson()[1]}\n\n"
        return self.days


lessons_day1 = [
    Lesson(lesson_name="Test1", cabinet=1),
    Lesson(lesson_name="Test2", cabinet=2),
    Lesson(lesson_name="Test3", cabinet=3)
]

lessons_day2 = [
    Lesson(lesson_name="Test4", cabinet=4),
    Lesson(lesson_name="Test5", cabinet=5),
    Lesson(lesson_name="Test6", cabinet=6)
]

lessons_day3 = [
    Lesson(lesson_name="Test7", cabinet=7),
    Lesson(lesson_name="Test8", cabinet=8),
    Lesson(lesson_name="Test9", cabinet=9)
]

lessons_day4 = [
    Lesson(lesson_name="Test10", cabinet=10),
    Lesson(lesson_name="Test11", cabinet=11),
    Lesson(lesson_name="Test12", cabinet=12)
]

lessons_day5 = [
    Lesson(lesson_name="Test13", cabinet=13),
    Lesson(lesson_name="Test14", cabinet=14),
    Lesson(lesson_name="Test15", cabinet=15)
]

work_week = [lessons_day1, lessons_day2, lessons_day3, lessons_day4, lessons_day5]

schedule = Schedule(work_week)

for day in schedule:
    print(f"{day_names[day.day_number]}")
    for lesson in day.day_lessons:
        print(f"Название: {lesson.get_lesson()[0].get_name()}\nКабинет: {lesson.get_lesson()[1]}\n")
