# Generated by Django 4.0.4 on 2022-05-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='help', max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='help')),
                ('completion_time', models.DateTimeField(help_text='help', null=True)),
                ('image_field', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='help', max_length=100)),
                ('description', models.TextField(help_text='help')),
                ('time_estimate', models.IntegerField(help_text='help')),
                ('completed', models.BooleanField(default=False)),
                ('image_field', models.ImageField(upload_to='images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
    ]
