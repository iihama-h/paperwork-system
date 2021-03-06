# Generated by Django 3.1 on 2021-10-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('name_kana', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('capital', models.IntegerField(blank=True, null=True)),
                ('postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fax_number', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('revenue', models.IntegerField(blank=True, null=True)),
                ('profit', models.IntegerField(blank=True, null=True)),
                ('number_of_employees', models.IntegerField(blank=True, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'clients',
                'ordering': ['-updated_datetime'],
            },
        ),
    ]
