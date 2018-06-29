from apscheduler.schedulers.background import BackgroundScheduler
from make_protocol import main

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(main, 'interval', minutes=15)
    scheduler.start()
