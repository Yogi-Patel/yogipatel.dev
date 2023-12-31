# Generated by Django 4.2.5 on 2023-09-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_project_lines_of_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lines_of_code',
            field=models.PositiveIntegerField(default=1, help_text='How many lines of code was this project?', verbose_name='Lines of Code'),
        ),
    ]
