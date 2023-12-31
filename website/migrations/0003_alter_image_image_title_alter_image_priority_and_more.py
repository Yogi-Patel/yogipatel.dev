# Generated by Django 4.2.5 on 2023-09-11 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_image_caption_remove_project_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_title',
            field=models.CharField(help_text='MAX_LENGTH = 150', max_length=150),
        ),
        migrations.AlterField(
            model_name='image',
            name='priority',
            field=models.DecimalField(decimal_places=2, help_text='MAXIMUM 3 digits and 2 decimal places', max_digits=3),
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, help_text='Optional. MAX_LENGTH = 150', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='code_url',
            field=models.URLField(blank=True, help_text='MAX_LENGTH = 300', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='deployment_url',
            field=models.URLField(blank=True, help_text='MAX_LENGTH = 300', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_title',
            field=models.CharField(help_text='MAX_LENGTH = 75', max_length=75),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=models.CharField(help_text='Try to reach 125 characters for uniform card sizes. MAX_LENGTH = 150', max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, help_text='Optional. MAX_LENGTH = 150', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='software_type',
            field=models.CharField(help_text='MAX_LENGTH = 50', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies_used',
            field=models.CharField(help_text='MAX_LENGTH = 150', max_length=150),
        ),
        migrations.AlterField(
            model_name='skill',
            name='priority',
            field=models.DecimalField(decimal_places=2, help_text='MAXIMUM 3 digits and 2 decimal places', max_digits=3),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_description',
            field=models.CharField(help_text='MAX_LENGTH = 75', max_length=75),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_title',
            field=models.CharField(help_text='MAX_LENGTH = 50', max_length=50),
        ),
    ]
