def find_next_multiple(number, multiple):
    remainder = number % multiple
    if remainder == 0:
        return number
    else:
        return number + (multiple - remainder)


def aplly_rounding_rules(number, next_multiple):
    if next_multiple == number:
        return number
    elif (next_multiple - number) < 3 and next_multiple >= 40:
        return next_multiple
    else:
        return number


def gradingStudents(grades):
    result = []
    for grade in grades:
        next_multiple = find_next_multiple(grade, 5)
        rounded_grade = aplly_rounding_rules(grade, next_multiple)
        result.append(rounded_grade)
    return result
