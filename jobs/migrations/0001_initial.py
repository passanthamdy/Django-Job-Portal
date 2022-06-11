# Generated by Django 4.0.5 on 2022-06-11 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('IN_PROGRESS', 'In Progress'), ('FINISHD', 'Finished')], max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
                ('Tags', models.ManyToManyField(to='tags.tag', verbose_name="Job's tags")),
                ('applied_developers', models.ManyToManyField(related_name='developers', to=settings.AUTH_USER_MODEL, verbose_name='Applied Developer')),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Accepted Developer')),
                ('job_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_owner', to=settings.AUTH_USER_MODEL, verbose_name='Job Owner')),
            ],
        ),
    ]
