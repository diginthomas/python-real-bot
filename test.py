from apscheduler.schedulers.background import BackgroundScheduler

def my_job():
    print("Hello from the scheduled job!")

scheduler = BackgroundScheduler()
scheduler.add_job(my_job, 'interval', seconds=10)
scheduler.start()