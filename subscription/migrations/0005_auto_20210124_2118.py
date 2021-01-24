# Generated by Django 3.1.5 on 2021-01-24 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0004_auto_20210124_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='target_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_target', to=settings.AUTH_USER_MODEL),
        ),
    ]
