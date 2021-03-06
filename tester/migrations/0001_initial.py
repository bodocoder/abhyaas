# Generated by Django 4.0 on 2021-12-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=32)),
                ('imageUrl', models.URLField(max_length=256)),
                ('optionA', models.CharField(default='A', max_length=1)),
                ('optionB', models.CharField(default='B', max_length=1)),
                ('optionC', models.CharField(default='C', max_length=1)),
                ('optionD', models.CharField(default='D', max_length=1)),
                ('correctOption', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
    ]
