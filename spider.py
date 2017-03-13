from urllib.request import urlopen #connect webpages in python
from link_finder import LinkFinder
from general import *

class Spider:

	# class variables (shared among all instances(spides)
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''  #text file .. save the data
	crawled_file = ''
	queue = set() #waiting list dont want to write every time to file
	crawled = set()


	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name

		Spider.queue_file = Spider.project_name + '/queue.txt'
		Spider.crawled_file = Spider.project_name + '/crawled.txt'
		self.boot()
		self.crawl_page('First spider', Spider.base_url)

	@staticmethod
	def boot():
		create_project_dir(Spider.project_name)
		create_data_files(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)

	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			print("Thread name" + thread_name + "now crawling "+ page_url)
			print('Queue ' + str(len(Spider.queue)) + " | Creawled "+ str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_links(page_url)) #set of all links in web page
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()


	@staticmethod
	def gather_links(page_url):
		html_string = ''
		try:
			response = urlopen(page_url) #return byte data
			if response.getheader('Content-Type') = 'text/html':
				html_bytes = response.read() #1s and 0s
				html_string = html_bytes.decode("utf-8") #convert to string te binary web data

			finder = LinkFinder(Spider.base_url,page_url)
			finder.feed(html_string)
		except:
			print("Error : can not crawled page")
			return set()

		return finder.page_links()









