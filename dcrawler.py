from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import os

class LinkParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for (key, value) in attrs:
				if key == 'href' and value not in ["javascript:void(0)","#"] and value.startswith("mailto")==False:
					newUrl = parse.urljoin(self.baseUrl, value)
					self.links = self.links + [newUrl]

	def getLinks(self, url):
		self.links = []
		self.baseUrl = url
		response = urlopen(url)
		if response.getheader('Content-Type').index('text/html')>-1:
			htmlBytes = response.read()
			htmlString = htmlBytes.decode("utf-8")
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "",[]

	def spider(self):
		url = input("Provide the link to start crawling for links e.g. \'http://example.com/\':  ")
		while url.startswith("http")==False and url[len(url)-1:]!='/':
			url = input("ERROR!!!\nProvide the link to start crawling for links e.g. \'http://example.com/\':  ")
		try:
			maxLinks = int(input("Enter the number of links(Enter 0 if no limit):  "))
			while maxLinks<0:
				maxLinks = int(input("Can't enter a negative number! Enter the number of links(Enter 0 if no limit):  "))
		except:
			print("Awww! You did not provided a integer value. Please run this function again")
			return

		linksToVisit = [url]
		numberVisited = 0
		visited = []
		f = open('myfile.txt','w')
		while (((len(list(set(visited + linksToVisit)))) <= maxLinks) or maxLinks==0) and linksToVisit != []:
			url = linksToVisit[0]
			linksToVisit = linksToVisit[1:]
			try:
				if url not in visited:
					parser = LinkParser()
					data, links = parser.getLinks(url)
					numberVisited = numberVisited +1
					print(numberVisited, "Visiting:", url)
					links = [item for item in links if (item not in visited and item!=url)]
					linksToVisit = linksToVisit + links
					if linksToVisit:
						linksToVisit = list(set(linksToVisit))
					if maxLinks!=0:
						linksToVisit = linksToVisit[:(maxLinks-len(visited))]
					print ("Total number of links parsed:",len(list(set(visited + linksToVisit))))
					visited.append(url)
					f.write(url)
					f.write('\n')
			except:
				pass
		print("Terminating the Spider!")
		for link in linksToVisit[:(maxLinks-len(visited))]:
			f.write(link)
			f.write('\n')
		f.close()
