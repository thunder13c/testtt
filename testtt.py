def load_students(filename):
    students = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(",")

        student = {
            "name": data[0],
            "score": int(data[1])
        }

        students.append(student)

    return students


filename = "rr.csv"
a = load_students(filename)
print(a)