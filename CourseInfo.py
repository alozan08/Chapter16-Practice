'''
    Define a Course base class with attrinutes number and title
    Define a print_info() method that displays the course number and title. Also define a derived class
    OfferedCourse with the additional attributes instructor_name, term, and class_time
    ex input:
        ECE287
        Digital Systems Design
        ECE387
        Embedded Systems Design
        Mark Patterson
        Fall 2018
        WF: 2-3:30 pm
    ex output:
        Course Information:
           Course Number: ECE287
           Course Title: Digital Systems Design
        Course Information:
           Course Number: ECE387
           Course Title: Embedded Systems Design
           Instructor Name: Mark Patterson
           Term: Fall 2018
           Class Time: WF: 2-3:30 pm
'''
class Course:
    def __init__(self, number, title):
        self.number = number
        self.title = title

    def print_info(self):
        print('Course Information:')
        print('   Course Number:', self.number)
        print('   Course Title:', self.title)

class OfferedCourse(Course):
    def __init__(self, number, title, instructor_name, term, class_time):
        Course.__init__(self, number, title)
        self.instructor_name = instructor_name
        self.term = term
        self.class_time = class_time

    def print_info(self):
        Course.print_info(self)
        print('   Instructor Name:', self.instructor_name)
        print('   Term:', self.term)
        print('   Class Time:', self.class_time)


if __name__ == "__main__":
    course_number = input()
    course_title = input()

    o_course_number = input()
    o_course_title = input()
    instructor_name = input()
    term = input()
    class_time = input()

    my_course = Course(course_number, course_title)
    my_course.print_info()

    my_offered_course = OfferedCourse(o_course_number, o_course_title, instructor_name, term, class_time)
    my_offered_course.print_info()

