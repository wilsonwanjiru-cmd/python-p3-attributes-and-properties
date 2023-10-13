#!/usr/bin/env python3

from person import Person  # Import the Person class from person.py

import io
import sys

class TestPerson:
    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(name='Guido', job='Sales')
        assert isinstance(guido, Person)

    def test_name_not_empty(self):
        '''prints "Name must be a string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="", job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    def test_name_string(self):
        '''prints "Name must be a string between 1 and 25 characters." if not a string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name=123, job='Sales')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    def test_name_length_over_25(self):
        '''prints "Name must be a string under 25 characters." if name length is over 25.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="This is a very long name that exceeds 25 characters", job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string under 25 characters.\n"

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person("Guido")
        assert guido.name == "Guido"

    def test_valid_name_title_case(self):
        '''converts name to title case and saves it if between 1 and 25 characters'''
        guido = Person(name="guido van rossum")
        assert guido.name == "Guido Van Rossum"

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in the job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Alice", job="Pilot")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Job must be in the list of approved jobs.\n"

    def test_valid_job(self):
        '''Does not print error message if job is valid.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Alice", job="Sales")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == ""

    def test_job_in_list(self):
        '''saves job if in the job list.'''
        guido = Person(job="Sales")
        assert guido.job == "Sales"

    def test_invalid_job(self):
        '''prints "Job must be in the list of approved jobs." if the job is invalid.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        person = Person(name="Bob", job="InvalidJob")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Job must be in the list of approved jobs.\n"


