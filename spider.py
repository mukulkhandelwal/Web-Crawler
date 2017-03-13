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


	def __init__(self):










