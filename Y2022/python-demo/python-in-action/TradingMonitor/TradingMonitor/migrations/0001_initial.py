# Generated by Django 4.0.3 on 2022-03-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', models.CharField(max_length=10)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
