from django.db import models


# class Group(models.Model):
#     name_group = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name_group
#
#
# class Book(models.Model):
#     name_book = models.CharField(max_length=100)
#     number_of_pages = models.CharField(max_length=10)
#     owner_book = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name_book
#
#
# class Student(models.Model):
#     book = models.ManyToManyField(Book, related_name='book_name')
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     age = models.CharField(max_length=10)
#     avatar = models.ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return self.firstname
#
#
# class Work(models.Model):
#     name_work = models.ForeignKey(Student, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#
#     def __str__(self):
#         return self.name_work



class Product(models.Model):
    name_product = models.CharField(max_length=100)
    cost_product = models.CharField(max_length=100)
    quantity_product = models.CharField(max_length=100)

    def __str__(self):
        return self.name_product


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.post