

class Student:
    """Here is a simple Student class to illustrate the following fundamental class
       features in Python:
       1) constructor (__init__() that defines private fields for first, last, gpa, and net_ID
       2) getter/accessor methods named based on the private field names but without the __
          which would make the methods private (we want them public)
       3) __str__() method which is used to return a string representation of the fields in
          your object (this is like toString() in Java)
       4) __eq__() method which lets us use == on two Student objects (this is like override of equals() in Java)
       5) __lt__() method which lets us use < on two Student objects (you would have to implement Comparable
          and call compareTo() in Java to get something like this!)
       6) __repr__() method which is used to provide a basic representation of a Student object. It often
          behaves like __str__() which is how it is implemented below. It is not mandatory to have this
          but it is handy when you want to know what an object of a class (Student in this case) is made of.
       7) set_first() method which assigns a new first name. If new_first is not a string a TypeError exception
          is generated"""
    def __init__(self, first, last, gpa, net_id):
        """This method is used to create an instance of a student, creating private fields (by using __)
           and initializing those fields to the values passed as parameters to the method"""
        self.__first = first
        self.__last = last
        self.__gpa = gpa
        self.__net_ID = net_id

    def first(self):
        """this method is an accessor/getter that returns the first name since the field __first is private"""
        return self.__first

    def last(self):
        """this method is an accessor/getter that returns the last name since it is private"""
        return self.__last

    def gpa(self):
        """this method is an accessor/getter that returns the gpa since it is private"""
        return self.__gpa

    def net_ID(self):
        """this method is an accessor/getter that returns the net_ID since it is private"""
        return self.__net_ID

    def set_first(self, new_first):
        """A simple setter/mutator to assign a new first name. If new_first is not a string an exception is raised"""
        if isinstance(new_first, str):
            self.__first = new_first
        else:
            raise TypeError("new_first passed to set_first was not a string")

    def __str__(self):
        """this method overrides the version from the object class and is called when you print a Student"""
        return "%s %s, gpa: %s, netID: %s" % (self.__first, self.__last, self.__gpa, self.__net_ID)

    def __repr__(self):
        """this method overrides the version from the object class"""
        return "%s %s, gpa: %s, netID: %s" % (self.__first, self.__last, self.__gpa, self.__net_ID)

    def __eq__(self, other):
        """this method overrides the version from the object class and lets you use == to compare Students"""
        if isinstance(other, Student):
            return self.__first == other.first() and self.__last == other.last() and self.__gpa == other.gpa() \
                   and self.__net_ID == other.net_ID()
        return False

    def __lt__(self, other):
        """ This method lets you compare two students for order -- if the Student object on the left
        hand side of the < is smaller than __lt__ returns true"""
        if isinstance(other, Student):
            if self.__last < other.__last:
                return True
            elif self.__last == other.__last and self.__first < other.__first:
                return True
            elif self.__last == other.__last and self.__first == other.__first and self.__net_ID < other.__net_ID:
                return True
            else:
                return False

        raise Exception("other argument to less than was not a Student: " % other)

    def __gt__(self, other):
        """ This method lets you compare two students for order -- if the Student object on the left
        hand side of the > is greater than __gt__ returns true"""
        if isinstance(other, Student):
            if self.__last > other.__last:
                return True
            elif self.__last == other.__last and self.__first > other.__first:
                return True
            elif self.__last == other.__last and self.__first == other.__first and self.__net_ID > other.__net_ID:
                return True
            else:
                return False

        raise Exception("other argument to greater than was not a Student: " % other)

    def __ge__(self, other):
        """ This method lets you compare two students for order -- if the Student object on the left
        hand side of the >= is greater than or equal to __ge__ returns true"""
        if isinstance(other, Student):
            if self.__last >= other.__last:
                return True
            elif self.__last == other.__last and self.__first >= other.__first:
                return True
            elif self.__last == other.__last and self.__first == other.__first and self.__net_ID >= other.__net_ID:
                return True
            else:
                return False

        raise Exception("other argument to greater than or equal to was not a Student: " % other)

    def __le__(self, other):
        """ This method lets you compare two students for order -- if the Student object on the left
        hand side of the <= is smaller than or equal to__le__ returns true"""
        if isinstance(other, Student):
            if self.__last <= other.__last:
                return True
            elif self.__last == other.__last and self.__first <= other.__first:
                return True
            elif self.__last == other.__last and self.__first == other.__first and self.__net_ID <= other.__net_ID:
                return True
            else:
                return False

        raise Exception("other argument to less than was not a Student: " % other)

    def __ne__(self, other):
        """this method overrides the version from the object class and lets you use != to compare Students"""
        if isinstance(other, Student):
            return self.__first != other.first() or self.__last != other.last() or self.__gpa != other.gpa() \
                   or self.__net_ID != other.net_ID()
        return False


# tests for our Student class

def test_init():
    """We must create students with first,last, gpa, and net_ID since that is the only init we have"""
    print("-----------------------------------------------------")
    print("__init__() (or constructor if you want to call it that) test")
    student = Student("joe", "student", 3.79, "jstudent1")
    print("assigned joe student 3.79 jstudent1 as fields for Student")
    print("Here is the result:", student)  # note that the print tests the __str__() method which is
    # called when you print a Student (student in this case)


def test_first_last_gpa_net_id_getters():
    print("-----------------------------------------------------")
    print("\nfirst(), last(), gpa(), net_ID() getter tests")
    student = Student("joe", "student", 3.79, "jstudent1")
    print(student.first())
    print(student.last())
    print(student.gpa())
    print(student.net_ID())
    if student.first() == "joe" and student.last() == "student" and student.gpa() == 3.79 \
    and student.net_ID() == "jstudent1":
        print("test PASSED")
    else:
        print("uh oh test FAILED")


def test_set_first():
    print("-----------------------------------------------------")
    print("testing set_first()")
    student = Student("joe", "student", 3.44, "jstudent1")
    print("student first name before set_first call: ", student.first())
    student.set_first("jack")
    print("assigned first name of 'jack' to student", student)
    if student.first() == "jack":
        print("test PASSED")
    else:
        print("test failed")

    print("now with something not a string")
    try:
        student.set_first(3.33333)
    except TypeError as type_error:
        print(type_error)
        print("TypeError exception generated as expected, test PASSED")


def test_eq():
    print("-----------------------------------------------------")
    print("\n__eq__() tests")
    stu1 = Student("tom", "smith", 3.23, "tsmith")
    stu2 = Student("tom", "smith", 3.33, "tomsmith")
    if stu1 == stu2:
        print(stu1, stu2, " are equal, test FAILED")
    else:
        print(stu1, stu2, "Not equal, test PASSED")

    stu3 = Student("tom", "smith", 3.23, "tsmith")
    if stu1 == stu3:
        print(stu1, stu3, "are equal, test PASSED")
    else:
        print(stu1, stu3, "not equal, test FAILED")


def test_lt():
    print("-----------------------------------------------------")
    print("__lt__() tests")
    stu1 = Student("tom", "smith", 3.23, "tsmith")
    stu2 = Student("tom", "smith", 3.33, "tomsmith")
    if stu1 < stu2:
        print(stu1, "is less, test FAILED")
    elif stu2 < stu1:
        print(stu2, "is less than, test PASSED")
    else:
        print(stu1, stu2, "are equal, test FAILED")


def test_gt():
    print("-----------------------------------------------------")
    print("__gt__() tests")
    stu1 = Student("tom", "smith", 3.23, "tsmith")
    stu2 = Student("tom", "smith", 3.33, "tomsmith")
    if stu1 > stu2:
        print(stu1, "is greater, test FAILED")
    elif stu2 > stu1:
        print(stu2, "is greater than, test PASSED")
    else:
        print(stu1, stu2, "are equal, test FAILED")


def test_ge():
    print("-----------------------------------------------------")
    print("__ge__() tests")
    stu1 = Student("tom", "smith", 3.23, "tsmith")
    stu2 = Student("tom", "smith", 3.33, "tomsmith")
    if stu1 >= stu2:
        print(stu1, "is greater than or equal to, test FAILED")
    elif stu2 >= stu1:
        print(stu2, "is greater than or equal to, test PASSED")
    else:
        print(stu1, stu2, "are equal, test PASSED")


def test_le():
    print("-----------------------------------------------------")
    print("__le__() tests")
    stu1 = Student("tom", "smith", 3.23, "tsmith")
    stu2 = Student("tom", "smith", 3.33, "tomsmith")
    if stu1 <= stu2:
        print(stu1, "is less than or equal to, test PASSED")
    elif stu2 <= stu1:
        print(stu2, "is less than or equal to, test FAILED")
    else:
        print(stu1, stu2, "are equal, test PASSED")


def test_ne():
    print("-----------------------------------------------------")
    print("__ne__() tests")
    stu1 = Student("tom", "smith", 3.23, "tsmith")
    stu2 = Student("tom", "smith", 3.33, "tomsmith")
    if stu1 == stu2:
        print(stu1, stu2, " are equal, test FAILED")
    else:
        print(stu1, stu2, "Not equal, test PASSED")

    stu3 = Student("tom", "smith", 3.23, "tsmith")
    if stu1 == stu3:
        print(stu1, stu3, "are equal, test FAILED")
    else:
        print(stu1, stu3, "not equal, test PASSED")


def test_sort_list():
    print("-----------------------------------------------------")
    print("sort list taking advantage of __eq__() and __lt__()")
    stu1 = Student("tom", "smith", 3.23, "tsmith")
    stu2 = Student("tom", "smith", 3.33, "tomsmith")
    students = [stu1, stu2, Student("bubba", "smith", 3.45, "bsmith")]
    students.sort()  # uses __eq__ and __lt__ automagically (we heart Python for things like this)
    print("should get bubba, then tomsmith, then tsmith printed")
    print(*students, sep="\n")  # prints all students in the list and separates them with a newline (uses __str__())


print("*************** NOW TESTING THE STUDENT CLASS *******************")
test_init()
test_first_last_gpa_net_id_getters()
test_set_first()
test_eq()
test_lt()
test_gt()
test_ge()
test_le()
test_ne()
test_sort_list()
print("*************** DONE TESTING ******************")
