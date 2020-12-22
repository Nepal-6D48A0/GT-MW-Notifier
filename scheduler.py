import schedule
import time
import scrape
import jobs_list


def run_schedule():
    scrape.main() #run the main method
    jobs_list.main() #run jobs_list
    print("done!")

schedule.every(20).seconds.do(run_schedule)

while 1:
    schedule.run_pending()
    time.sleep(1)
    