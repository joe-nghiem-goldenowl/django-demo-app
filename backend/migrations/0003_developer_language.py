# Generated by Django 4.0.3 on 2022-03-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_developer_project_project_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='language',
            field=models.CharField(choices=[('py', 'Python'), ('cpp', 'C++'), ('cs', 'C#'), ('java', 'Java'), ('js', 'JavaScript'), ('other', 'Other')], default='other', max_length=5),
        ),
    ]
