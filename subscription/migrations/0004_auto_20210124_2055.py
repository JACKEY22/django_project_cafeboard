# Generated by Django 3.1.5 on 2021-01-24 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('subscription', '0003_auto_20210124_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='shop.shop'),
        ),
    ]
