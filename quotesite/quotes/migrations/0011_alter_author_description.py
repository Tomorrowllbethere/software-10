# Generated by Django 5.0.6 on 2024-06-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0010_author_author_description_idx"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="description",
            field=models.TextField(),
        ),
    ]
