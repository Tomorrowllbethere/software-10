# Generated by Django 5.0.6 on 2024-06-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0006_alter_author_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="description",
            field=models.CharField(max_length=5000, unique=True),
        ),
    ]
