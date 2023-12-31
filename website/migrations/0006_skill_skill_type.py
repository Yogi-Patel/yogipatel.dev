# Generated by Django 4.2.5 on 2023-09-14 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_contact_last_name_alter_contact_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_type',
            field=models.IntegerField(choices=[('1', 'Programming Language'), ('2', 'Programming Framework'), ('3', 'Tools'), ('4', 'Other')], default=0, help_text='Skill type decides which one to show first', verbose_name='Skill Type'),
            preserve_default=False,
        ),
    ]
