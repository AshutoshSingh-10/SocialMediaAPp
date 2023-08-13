# Generated by Django 4.1.1 on 2023-08-13 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_alter_userprofile_avatar'),
        ('comments', '0002_commentreply'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile')),
                ('likeOn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
            ],
            options={
                'unique_together': {('commentUser', 'likeOn')},
            },
        ),
    ]