# Generated by Django 4.1.5 on 2023-04-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("block", "0002_group_serv_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="serv_acc_id",
            field=models.CharField(default="Not Available", max_length=230),
            preserve_default=False,
        ),
    ]
