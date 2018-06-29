from apscheduler.schedulers.blocking import BlockingScheduler
from make_protocol import main


scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', minutes=30)
scheduler.start()
