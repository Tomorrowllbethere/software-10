# Generated by Django 5.0.6 on 2024-06-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0003_alter_author_description_alter_quote_quote_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="description",
            field=models.CharField(max_length=800, unique=True),
        ),
    ]