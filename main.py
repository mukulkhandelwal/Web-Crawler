import threading 
from queue import Queue

from spider import Spider
from domain import *
from general import *


PROJECT_NAME = '' #put the name of project like google
HOMEPAGE = '' #put url of the project just like https://google.com
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#create worker threads (will die when main exits)

def create_workers():
	for _ in range(NUMBER_OF_THREADS): # _ dont care of value 
		t = threading.Thread(target=work)
		t.daemon = True #die whenever main exit
		t.start()


# DO the next job in the queue
def work():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name,url)
		queue.task_done()

#each queued link is a new job
def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()



#check if there are items in the queue ,if so crawl them
def crawl():
	queued_links = file_to_set(QUEUE_FILE)

	if len(queued_links) > 0:
		print(str(len(queued_links)) + ' links in the queue')
		create_jobs()


create_workers()
crawl()	



