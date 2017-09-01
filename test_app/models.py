import os

from django.utils.timezone import now as timezone_now
from django.db import models


TYPE_CHOICES = (
        ('o+', "O+"),
        ('A+', "A+")
    )

def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return "quotes/%s%s" % (now.strftime("%Y/%m/%Y%m%d%H%M%S"), filename_ext.lower(),)


class Customer(models.Model):

    name = models.CharField(max_length=55, verbose_name="Customer Name")
    email = models.EmailField(max_length=75, verbose_name="Email")
    phone = models.CharField(max_length=14, verbose_name="Contact")
    address = models.CharField(max_length=150, verbose_name="Address", blank=True)
    blood_group = models.CharField(max_length=50, choices=TYPE_CHOICES)
