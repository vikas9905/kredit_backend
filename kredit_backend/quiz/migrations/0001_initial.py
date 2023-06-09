# Generated by Django 3.2.15 on 2023-04-02 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ammount_requested', models.IntegerField(default=0)),
                ('used_coin', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quizs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('num_of_ques', models.IntegerField()),
                ('total_coins', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('total_coins', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserPaymentOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('payment_num', models.IntegerField()),
                ('verified', models.BooleanField(default=False)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.paymentprovider')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.user')),
            ],
        ),
        migrations.CreateModel(
            name='QuizTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_ans', models.IntegerField()),
                ('incorrect_ans', models.IntegerField()),
                ('earned_coins', models.IntegerField()),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizs')),
                ('user_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.user')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('level', models.IntegerField()),
                ('coins', models.IntegerField()),
                ('quiz_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quizs')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.questiontag')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount_paid', models.IntegerField()),
                ('payment_status', models.BooleanField(default=False)),
                ('for_coins', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.orderdetails')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='payment_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.userpaymentoptions'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.user'),
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionNum', models.CharField(max_length=10)),
                ('optionValue', models.CharField(max_length=200)),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.options')),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
            ],
        ),
    ]
