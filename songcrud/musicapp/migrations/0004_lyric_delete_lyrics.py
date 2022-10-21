# Generated by Django 4.1.2 on 2022-10-15 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_lyrics_remove_song_title_delete_lyics_lyrics_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('Song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
            ],
        ),
        migrations.DeleteModel(
            name='Lyrics',
        ),
    ]