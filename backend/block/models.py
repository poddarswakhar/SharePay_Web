from django.db import models

# Create your models here.


# model for user signup based
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

    def __str__(self):
        return self.name + " " + self.email
