# Generated by Django 4.1 on 2022-12-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(name="accounts", managers=[],),
        migrations.AlterField(
            model_name="accounts",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="accounts",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
    ]
