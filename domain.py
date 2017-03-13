from urllib.parse import urlparse


#get domain name (example.com)#return only last two

def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		#print(results[-2] + '.' + results[-1])
		return results[-2] + '.' + results[-1]
	except:
		return ''


# Get sub domain name(name.example.com)

def get_sub_domain_name(url):
	try:
		print(url)
		return urlparse(url).netloc 
	except:
		return ''


#print(get_domain_name('https://thenewboston.com/index.php'))
