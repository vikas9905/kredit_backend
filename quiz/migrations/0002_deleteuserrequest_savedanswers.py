# Generated by Django 3.2.15 on 2023-04-22 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteUserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=30)),
                ('reason', models.CharField(max_length=200)),
                ('feedback', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SavedAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.options')),
                ('qid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizs')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.user')),
            ],
        ),
    ]
