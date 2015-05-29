# Dcrawler
A web crawler developed using Python 3 for parsing links.

NOTE: This web crawler has been developed using Python 3, kindly install Python 3 before using it.

Step 1: Go to the directory in which dcrawler.py is there.

Step 2: Open Python 3 shell.

Step 3: You'll need to import the Class inside the file 'dcrawler.py'. Run the command 'from dcrawler import LinkParser'

Step 4: After importing the Class, you need to create an object of that Class. For that run the command 'obj = LinkParser()'. 'obj' is the name of the object.

Step 5: After creating the object, you need to call the function which will start crawling. For that run the command ' obj.spider()'

Step 6: After completing the step 6, you'll bes asked to enter a link from which you want to start crawling. Kindly note that the URL that you provide must start with "http" and end with '/'.

Step 7: After completing the step 6, you'll be asked to enter the number of links you want to parse. Enter 0 if you want all the links.

After a link has been visited, it'll be logged in the file 'myfile.txt'. After the crawler achieves the target of parsing the number of links it'll start logging them in the same file.

After visiting a page you'll be informed how many links has been parsed. Also you'll be informed about the number of link and the link that is being visited.
