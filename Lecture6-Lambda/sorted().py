###sortirane po dadena logika = sorted(iterable, key, reversed)

student_grades = {'Ivan': [3, 4], 'Peter': [5, 2, 5], 'CMaria': [6, 6, 4, 3]}


#### tuk sortirame po 2 razlichni parametyra !!!
sorted_grades = sorted(student_grades.items(), key=lambda value_list: (len(value_list[1]), value_list[0] ))

# for key, value in student_grades.items():
#     #print(len(student_grades[value]))
#     print(len(value))

for name , grades in sorted_grades:
    print(name, grades)

print(type(sorted_grades))