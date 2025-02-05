# Generated by Django 5.0.6 on 2024-07-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyers', '0002_addjob_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='addjob',
            options={'ordering': ['salary']},
        ),
        migrations.AddField(
            model_name='addjob',
            name='job_category',
            field=models.ManyToManyField(to='Buyers.category'),
        ),
    ]
