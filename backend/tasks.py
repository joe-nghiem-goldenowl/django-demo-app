from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule

schedule, _ = IntervalSchedule.objects.get_or_create(
    every=15,
    period=IntervalSchedule.MINUTES,
)

PeriodicTask.objects.get_or_create(
    interval=schedule,
    name='Update currency rate',
    task='demo.celery.update_currency_rate',
)