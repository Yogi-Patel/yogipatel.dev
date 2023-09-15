# Generated by Django 4.2.5 on 2023-09-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_contact_email_alter_contact_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, help_text='Optional.', max_length=150, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, help_text='Optional.', max_length=150, null=True, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='project',
            name='code_url',
            field=models.URLField(blank=True, help_text='Optional. MAX_LENGTH = 300', max_length=300, null=True, verbose_name='Code URL'),
        ),
        migrations.AlterField(
            model_name='project',
            name='deployment_url',
            field=models.URLField(blank=True, help_text='Optional. MAX_LENGTH = 300', max_length=300, null=True, verbose_name='Deployment URL'),
        ),
    ]
