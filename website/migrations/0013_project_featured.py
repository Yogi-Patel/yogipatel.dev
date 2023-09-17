# Generated by Django 4.2.5 on 2023-09-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_project_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=True, help_text='Is it okay if this project shows up on the home page?', verbose_name='Featured Project'),
        ),
    ]
