# Generated by Django 4.1.5 on 2023-02-02 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="notes",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
