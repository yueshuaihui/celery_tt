from datetime import timedelta
from celery.schedules import crontab

broker_url = "redis://:124676@172.16.75.125:6379/0"  # 指定broker
result_backend = "redis://:124676@172.16.75.125:6379/1"  # 指定backend
timezone = 'Asia/Shanghai'  # 指定时区

task_annotations = {
    "mm.task1.add": {"rate_limit": "6/m"}
}

# 指定导入的任务模块
imports = (
    'mm.task1',
    'mm.task2'
)

beat_schedule = {
    # 'add-every-5-seconds': {
    #     'task': 'mm.task1.add',
    #     'schedule': timedelta(seconds=2),  # 每 30 秒执行一次
    #     'args': (5, 5)  # 任务函数参数
    # },
    'add-every-10-seconds': {
        'task': 'mm.task2.add2',
        'schedule': crontab(minute="*"),  # 每一分钟执行一次
        'args': (8, 8)  # 任务函数参数
    }
}
