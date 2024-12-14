from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'race2space.settings')

app = Celery('race2space')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-news-every-hour': {
        'task': 'home.tasks.update_news',
        'schedule': 3600.0,  # 1 hour in seconds
    },
}
