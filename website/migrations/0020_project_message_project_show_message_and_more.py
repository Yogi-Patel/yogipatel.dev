# Generated by Django 4.2.5 on 2023-09-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_image_priority_alter_skill_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='message',
            field=models.CharField(blank=True, help_text='MAX_LENGTH = 250', max_length=250, null=True, verbose_name='Additional Message'),
        ),
        migrations.AddField(
            model_name='project',
            name='show_message',
            field=models.BooleanField(default=False, help_text='Do you want to show an additional message?', verbose_name='Show message?'),
        ),
        migrations.AddField(
            model_name='project',
            name='show_project',
            field=models.BooleanField(default=True, help_text='Do you want the project to show up on the website?', verbose_name='Show Project'),
        ),
    ]
