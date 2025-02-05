# Generated by Django 5.0.6 on 2024-07-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('part-tyme', 'part-time'), ('Full-time', 'Full-time')], max_length=100)),
                ('job_details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
