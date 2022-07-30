from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    last_four = models.IntegerField()
    email = models.CharField(max_length=200, blank=True)
    admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Transaction(models.Model):
    drop_off = models.DateTimeField(blank=True)
    admin = models.ForeignKey(User, related_name='user_admin', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="transactions")

    def __str__(self):
        return f"{self.admin} helped {self.customer}"

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Item(models.Model):
    drop_off = models.DateTimeField(blank=True)
    due_off = models.DateTimeField(blank=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, related_name="items")
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.drop_off}"

