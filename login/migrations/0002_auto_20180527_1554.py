# Generated by Django 2.0.5 on 2018-05-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id_question',
            field=models.CharField(max_length=50, verbose_name='Can I have your name, genius?'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name_asker',
            field=models.CharField(max_length=50, verbose_name='Ask me anything babe!'),
        ),
    ]