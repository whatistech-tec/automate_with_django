from .celery import app as celery_app


#load up the celery app once django starts
__all__ = ('celery_app',)