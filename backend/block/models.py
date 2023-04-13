from django.db import models

# Create your models here.


# model for user signup based
from django.forms import forms


class Group(models.Model):
    id = models.AutoField(primary_key=True)

    user1_name = models.CharField(max_length=230)
    user1_wal = models.CharField(max_length=230)

    user2_name = models.CharField(max_length=230)
    user2_wal = models.CharField(max_length=230)

    user3_name = models.CharField(max_length=230)
    user3_wal = models.CharField(max_length=230)

    dest_wal = models.CharField(max_length=230)

    ind_val = models.FloatField()

    serv_name = models.CharField(max_length=230)

    serv_acc_id = models.CharField(max_length=230)

    ren = models.DateTimeField(auto_now_add=True)

    contract_address = models.TextField(max_length=45, null=True, default=None)

    abi = models.JSONField(null=True, default=None)

    def __str__(self):
        return self.name + " " + self.email
