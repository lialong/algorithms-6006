def birthday_match(students):
    n = len(students)
    record = StaticArray(n)
    for k in range(n):
        (name1, bday1) = students[k]
        for i in range(k):
            (name2, bday2) = students[i]
            if bday1 == bday2:
                return (name1, name2)
        record.set_at(k, (name1, bday1))
    return None
