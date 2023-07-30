# Generated by Django 4.2.3 on 2023-07-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauthen', '0006_user_country_user_date_of_birth_user_diabetic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.TextField(max_length=100)),
                ('standard', models.TextField(max_length=40, null=True)),
                ('carb', models.IntegerField(null=True)),
                ('sugar', models.IntegerField(null=True)),
                ('fat', models.IntegerField(null=True)),
                ('calorie', models.IntegerField(null=True)),
            ],
        ),
    ]