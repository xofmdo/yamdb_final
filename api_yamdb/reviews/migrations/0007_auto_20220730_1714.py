# Generated by Django 2.2.16 on 2022-07-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220730_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('title', 'author')},
        ),
    ]
