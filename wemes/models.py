from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    last_four = models.IntegerField()
    email = models.CharField(max_length=200, blank=True)
    admin = models.BooleanField(default=False)
    code = models.ImageField(blank=True, upload_to="code")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        qr_image = qrcode.make(f'http://127.0.0.1:8000/users/{self.id}/')
        qr_offset = Image.new('RGB', (350,350), 'white')
        qr_offset.paste(qr_image)
        file_name = f'{self.last_four}-{self.first_name}_{self.last_name}_qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.code.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

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

