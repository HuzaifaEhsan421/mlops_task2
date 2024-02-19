# test.py
import pytest
from main import StudentsInMLOps

@pytest.fixture
def students_mlops():
    return StudentsInMLOps()

def test_enroll_students(students_mlops):
    students_mlops.enrollStudents(5)
    assert students_mlops.getTotalStrength() == 5

def test_drop_students(students_mlops):
    students_mlops.enrollStudents(10)
    students_mlops.dropStudents(3)
    assert students_mlops.getTotalStrength() == 7

def test_get_class_name(students_mlops):
    assert students_mlops.getClassName() == "StudentsInMLOps_DS-N"
