# Generated by Django 2.2.6 on 2019-10-29 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_c', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_q', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AddField(
            model_name='feedback_choice',
            name='feedback_q',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Feedback_Question'),
        ),
    ]
