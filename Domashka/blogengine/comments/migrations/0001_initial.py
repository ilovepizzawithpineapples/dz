# Generated by Django 2.2.1 on 2019-05-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COMMENTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.TextField(blank=True, db_index=True)),
                ('body_comment', models.TextField(blank=True, db_index=True)),
            ],
        ),
    ]