# Generated by Django 4.2.7 on 2023-12-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=15)),
                ('task', models.ManyToManyField(to='tasks.mytask')),
            ],
        ),
    ]