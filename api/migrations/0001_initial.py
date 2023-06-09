# Generated by Django 4.1.7 on 2023-03-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('Brahmanbaria', 'Brahmanbaria'), ('Cummilla', 'Cummilla'), ('Feni', 'Feni'), ('Laxmipur', 'Laxmipur'), ('Noakhali', 'Noakhali'), ('Chittagong', 'Chittagong'), ('Coxsbazar', 'Coxsbazar'), ('Faridpur', 'Faridpur'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi')], max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, upload_to='Profile_Image')),
                ('resume_doc', models.FileField(blank=True, upload_to='Resume_files')),
            ],
        ),
    ]
