import newspaper
import os
from flask import Flask
def clear():
	os.system('clear')  # For Linux/OS X
app = Flask('app')
continueBool = True
print("     HENRYMARTIN4's News App")
print("===================================")
while continueBool:
	urlNum = input("Input the number representing the news website you want - options are:\n1. https://www.cnn.com\n2. https://bbc.co.uk\n3. https://fox13now.com\n  >")
	if urlNum == "1":
		url = "http://www.cnn.com"
		continueBool = False		
	elif urlNum == "2":
		url = "http://bbc.co.uk"
		continueBool = False		
	elif urlNum == "3":
		url = "http://fox13now.com"
		continueBool = False
	else:
		print("Input a valid number!")
clear()
paper = newspaper.build(url)
i = 0
print("            Articles")
print("===================================")
for article in paper.articles:
	article.download()
	article.parse()
	print(str(i)+". "+article.title)
	i = i + 1
articleNum = int(input("Enter article number to view: "))
article = paper.articles[articleNum]
article.download()
article.parse()
@app.route('/')
def main():
  return article.html
clear()
app.run(host='0.0.0.0', port=8080)
