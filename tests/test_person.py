from __future__ import annotations
from actions.person import Person
import pytest

@pytest.fixture
def person():
    return Person('Andreas Werdich', 52, jobs=['Software Engineer'])

def test_init(person: Person):
    assert person.name == 'Andreas Werdich'
    assert person.age == 52
    assert person.jobs == ['Software Engineer']

def test_first_name(person: Person):
    assert person.first_name == 'Andreas'

def test_last_name(person: Person):
    assert person.last_name == 'Werdich'

def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 53

def test_add_job(person: Person):
    person.add_job('QA Engineer')
    assert 'QA Engineer' in person.jobs