# Student
# Program that stores student name and list her courses and grades in a dict
# Author: Fatima Oliveira

student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99
        }
    ]
}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))