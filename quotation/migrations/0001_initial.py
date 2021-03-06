# Generated by Django 3.1 on 2021-10-05 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotations',
            fields=[
                ('quotation_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('expiry', models.CharField(blank=True, default='ご下命後1ヶ月間', max_length=255, null=True)),
                ('recipient', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_time', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_location', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_method', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_condition', models.CharField(blank=True, max_length=255, null=True)),
                ('consumption_tax', models.IntegerField(blank=True, default=0, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('client_id', models.ForeignKey(db_column='client_id', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='client.clients')),
                ('username', models.ForeignKey(db_column='username', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'quotations',
                'ordering': ['-updated_datetime'],
            },
        ),
        migrations.CreateModel(
            name='Quotations_attached_file',
            fields=[
                ('quotation_id', models.OneToOneField(db_column='quotation_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='quotation.quotations')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'quotations_attached_file',
            },
        ),
        migrations.CreateModel(
            name='Quotations_details',
            fields=[
                ('item_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('merchandise', models.CharField(blank=True, max_length=255, null=True)),
                ('merchandise_description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_unit_price', models.IntegerField(default=0)),
                ('purchase_unit_price', models.IntegerField(default=0)),
                ('order', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('quotation_id', models.ForeignKey(db_column='quotation_id', on_delete=django.db.models.deletion.CASCADE, to='quotation.quotations')),
            ],
            options={
                'verbose_name_plural': 'quotations_details',
                'ordering': ['order'],
            },
        ),
    ]
