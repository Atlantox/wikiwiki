# Generated by Django 4.1.7 on 2023-03-22 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_summary_title'),
        ('comments', '0003_alter_author_options_alter_author_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritearticles',
            name='articles',
            field=models.ManyToManyField(blank=True, to='articles.article', verbose_name='Favourite articles'),
        ),
    ]
