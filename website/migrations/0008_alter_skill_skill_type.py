# Generated by Django 4.2.5 on 2023-09-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_skill_skill_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_type',
            field=models.IntegerField(choices=[(1, 'Programming Language'), (2, 'Programming Framework'), (3, 'Tool'), (4, 'Other')], help_text='Skill type decides which one to show first', verbose_name='Skill Type'),
        ),
    ]
