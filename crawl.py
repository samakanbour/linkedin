from bs4 import BeautifulSoup

text = open('Sam Adi.html').read().replace('\n','')
soup = BeautifulSoup(text, 'html.parser')

# Experience
print [t.get_text() for t in soup.select('span.background-details ul li div.pv-entity__summary-info h3')]

# Skills
print [t.get_text() for t in soup.select('span.pv-skill-entity__skill-name.truncate')]

# Languages
print [t.get_text() for t in soup.select('span.pv-skill-entity__skill-name.truncate')]
