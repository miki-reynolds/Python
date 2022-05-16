class Course:
    def __init__(self, name, grade, credits):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    @property
    def name(self):
        return self.__name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        if grade > self.__grade:
            self.__grade = grade

    @property
    def credits(self):
        return self.__credits
    

class CourseRecords:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, name, gr, cr):
        if name not in self.__courses:
            self.__courses[name] = Course(name, gr, cr)
        else:
            if self.__courses[name].grade < gr:
                self.__courses[name].grade = gr
    
    def course_data(self, name):
        if name not in self.__courses:
            return f"no entry for this course"

        course = self.__courses[name]
        return f"{name} ({course.credits} cr) grade {course.grade}"

    def course_stats(self):
        courses = len(self.__courses)
        cr = 0
        grades = []

        for name in self.__courses.keys():
            cr += self.__courses[name].credits
            grades.append(self.__courses[name].grade)

        mean = 0
        if courses != 0:
            mean = sum(grades)/courses

        distri = ""
        for i in range(5, 0, -1):
            count = (grades.count(i)) * "x"
            distri += f"{i}: {count}\n"
        
        result = f"{courses} completed courses, a total of {cr} credits\n" + f"mean {mean:.1f}\n" + f"grade distribution\n" + distri

        return result

class CourseRecordsApplication:
    def __init__(self):
        self.__app = CourseRecords()

    def help(self):
        print("1 add course \n2 get course data \n3 statistics \n0 exit")

    def add_course(self):
        name = input("course: ")
        gr = int(input("grade: "))
        cr = int(input("credits: "))
        self.__app.add_course(name, gr, cr)

    def course_data(self):
        name = input("course: ")
        print(self.__app.course_data(name))

    def course_stats(self):
        print(self.__app.course_stats())
    
    def execute(self):
        self.help()
        while True:
            print("")
            cmmd = input("command: ")
            if cmmd == "0":
                break
            elif cmmd == "1":
                self.add_course()
            elif cmmd == "2":
                self.course_data()
            elif cmmd == "3":
                self.course_stats()
            else:
                self.help()

records = CourseRecordsApplication()
records.execute()


