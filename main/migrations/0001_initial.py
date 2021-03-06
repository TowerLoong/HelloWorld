# Generated by Django 2.2.4 on 2020-04-27 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='メモ')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
            ],
            options={
                'verbose_name': 'Memo Table',
                'verbose_name_plural': 'Memos Table',
                'db_table': 'memo',
            },
        ),
    ]
