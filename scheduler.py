from apscheduler.schedulers.blocking import BlockingScheduler
from make_protocol import main

scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', hours=1)
scheduler.start()
