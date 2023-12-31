# Generated by Django 3.1.2 on 2023-06-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230623_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('card_holder', models.CharField(max_length=100)),
                ('expiry_date', models.CharField(max_length=10)),
                ('cvv', models.CharField(max_length=3)),
            ],
        ),
    ]
