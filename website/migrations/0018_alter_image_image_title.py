# Generated by Django 4.2.5 on 2023-09-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_image_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_title',
            field=models.CharField(blank=True, help_text='MAX_LENGTH = 150. OPTIONAL', max_length=150, null=True, verbose_name='Image Title'),
        ),
    ]
