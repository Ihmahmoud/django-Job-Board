# Generated by Django 3.1.4 on 2021-01-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default=1, upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
