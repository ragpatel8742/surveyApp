# Generated by Django 3.1.2 on 2020-10-11 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('survey_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('survey_name', models.CharField(max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_question_id', models.IntegerField()),
                ('survey_question', models.CharField(max_length=100)),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_module.survey')),
            ],
            options={
                'unique_together': {('survey_question_id', 'survey_id')},
            },
        ),
        migrations.CreateModel(
            name='SurveyResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField()),
                ('answered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_module.survey')),
                ('survey_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_module.surveyquestions')),
            ],
        ),
    ]