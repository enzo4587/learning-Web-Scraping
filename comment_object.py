# Importing BeautifulSoup
from bs4 import BeautifulSoup

# Creating the document
markup = "<b><!--comment--></b>"

# Intialize the object with the document
soup = BeautifulSoup(markup, "html.parser")

# Get the whole comment inside the b tag
comment = soup.b.string

# Print the type of the comment
print(type(comment))


# output <class 'bs4.element,Comment'> meaning the comment variable contains a BeautifulSoup Comment object
# which you can further extract or manipulate to get the text you need.