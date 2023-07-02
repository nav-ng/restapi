from django.db import models


# Create your models here.


class TodoModel(models.Model):
    task_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    completed_status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


# class StudentModel(models.Model):
#     student_id = models.IntegerField()
#     student_name = models.CharField(max_length=100)
#     student_address = models.CharField(max_length=100)


class PersonModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()


# class EmployeeModel(models.Model):
#     name = models.CharField(max_length=50)
#     salary = models.IntegerField()
#     department = models.CharField(max_length=50)
#     designation = models.CharField(max_length=50)
#     company = models.CharField(max_length=50)


class MovieModel(models.Model):
    movie_name = models.CharField(max_length=50)
    no_of_seats = models.IntegerField()
    theatre_name = models.CharField(max_length=50)
    rating = models.IntegerField()


# class BookModel(models.Model):
#     book_name = models.CharField(max_length=50)
#     isbn_no = models.IntegerField()
#     author = models.CharField(max_length=50)
#     type = models.CharField(max_length=50)


class CompanyModel(models.Model):
    ceo_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    address = models.CharField(max_length=100)
    hr_name = models.CharField(max_length=50)
