from django.db import models
from datetime import datetime
import random
import string

class flodata_user(models.Model):
    uid=models.IntegerField(max_length=100,primary_key=True)
    user_id=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    account_id=models.IntegerField(max_length=100)
    time_zone=models.CharField(max_length=100)
    active_flag=models.BooleanField()
    created_date = models.DateTimeField(default=datetime.now())
    created_by = models.CharField(max_length=100)
    modified_date=models.DateTimeField(default=datetime.now())
    modified_by=models.CharField(max_length=100)
    reset_token=models.CharField(max_length=100)
    default_value=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    secret_key=models.CharField(max_length=100,default=default_value)
    email_id=models.EmailField(max_length=100)
    account_locked=models.BooleanField()

    class Meta:
        db_table='dataflo_user'