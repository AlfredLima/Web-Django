# Generated by Django 2.0.2 on 2018-02-08 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication', models.TextField()),
                ('data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('since', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('publications', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='snippets.Publications')),
            ],
        ),
    ]
