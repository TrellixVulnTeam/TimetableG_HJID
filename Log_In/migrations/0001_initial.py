# Generated by Django 2.1.7 on 2019-05-15 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('Register', '0009_auto_20190516_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('Lect_No', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('CellPhone_No', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredStaffs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_no', models.IntegerField(max_length=100)),
                ('Course_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_No', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('CellPhone_No', models.IntegerField()),
            ],
        ),
    ]
