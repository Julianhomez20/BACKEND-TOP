# Generated by Django 5.1.2 on 2024-10-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topeducation', '0007_companies_company_img_platforms_platform_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='certifition_platform_img',
            field=models.TextField(blank=True, default='None', null=True),
        ),
    ]