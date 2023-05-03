# Generated by Django 4.1.6 on 2023-03-15 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_newtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='preprocessedimages',
            name='image_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newtable', to='api.newtable'),
        ),
    ]