# Generated by Django 5.0.4 on 2024-04-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoldRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('akgsma', models.IntegerField()),
                ('kjf', models.IntegerField()),
                ('s_bhavan', models.IntegerField()),
                ('thirchur', models.IntegerField()),
                ('kgsda', models.IntegerField()),
                ('category', models.CharField(choices=[('22k', '22k'), ('24k', '24k')], max_length=50)),
                ('added_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]