# Generated by Django 2.1.5 on 2019-11-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myClassrooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voteNo', models.IntegerField(null=True)),
                ('className', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myClassrooms.Classes')),
            ],
        ),
        migrations.RemoveField(
            model_name='classrooms',
            name='course',
        ),
        migrations.RemoveField(
            model_name='classrooms',
            name='upVote',
        ),
        migrations.AddField(
            model_name='vote',
            name='classroomName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myClassrooms.Classrooms'),
        ),
    ]
