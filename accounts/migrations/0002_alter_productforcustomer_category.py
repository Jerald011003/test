# Generated by Django 4.1.2 on 2022-11-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productforcustomer',
            name='category',
            field=models.CharField(choices=[('McDonalds', 'McDonalds'), ('Jollibee', 'Jollibee'), ('Chowking', 'Chowking'), ('Coco', 'Coco')], max_length=200, null=True),
        ),
    ]