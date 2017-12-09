file_access = open("student-mat.csv", "r")
student_data = file_access.read()
all_students = student_data.split("\n") 