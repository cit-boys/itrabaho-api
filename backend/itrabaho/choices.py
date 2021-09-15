from typing import Match
from django.db.models import TextChoices
from django.db.models.enums import IntegerChoices


class SexChoices(TextChoices):
    MALE = ("M", "Male")
    FEMALE = ("F", "Female")


class StatusChoices(TextChoices):
    EMPLOYED = ("E", "Employed")
    UNEMPLOYED = ("U", "Unemployed")


class AcademicLevelChoices(TextChoices):
    NONE = ("N", "None")
    GRADE_SCHOOL = ("G", "Grade School")
    HIGH_SCHOOL = ("H", "High School")
    ASSOCIATE_DEGREE = ("A", "Associate Degree")
    BACHELORS_DEGREE = ("B", "Bachelor's Degree")
    MASTERS_DEGREE = ("M", "Master's Degree")
    DOCTORATE = ("D", "Doctorate")


class ActivityTypeChoices(TextChoices):
    MATCH = ("M", "Match")
    REVIEW = ("R", "Review")
    ACCEPTED = ("A", "Accepted")