# Generated by Django 4.1.5 on 2023-04-08 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user1_name", models.CharField(max_length=230)),
                ("user1_wal", models.CharField(max_length=230)),
                ("user2_name", models.CharField(max_length=230)),
                ("user2_wal", models.CharField(max_length=230)),
                ("user3_name", models.CharField(max_length=230)),
                ("user3_wal", models.CharField(max_length=230)),
                ("dest_wal", models.CharField(max_length=230)),
                ("ind_val", models.FloatField()),
            ],
        ),
    ]
