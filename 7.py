
dict_school = {}
students = {'Johnny', 'Bilbo', 'Steven', 'Knedrik', 'Aaron'}
grades = [[5,3,3,5,4,], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
a = [5,3,3,5,4,]
a_1 =sum(a) / len(a)
b = [2,2,2,3]
b_1 = sum(b) / len(b)
c = [4,5,5,2]
c_1 = sum(c) / len(c)
d = [4,4,3]
d_1 = sum(d) / len(d)
e = [5,5,5,4,5]
e_1 = sum(e) / len(e)

grades_new = [a_1, b_1, c_1, d_1, e_1]
list_students = list(students)
dict_school = dict(zip(list_students, grades_new))

print(dict_school)
