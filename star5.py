import bs4
from bs4 import BeautifulSoup
from csv import writer


# href links from a containers on local/ma page, href links from div containers on multiple location links
html = '''
<a class="c-directory-list-content-item-link" href="ma/auburndale/2040-commonwealth-ave.html" data-ya-track="links_directory">Auburndale</a>, 
<a class="c-directory-list-content-item-link" href="ma/belmont/535-trapelo-rd.html" data-ya-track="links_directory">Belmont</a>,
<a class="c-directory-list-content-item-link" href="ma/brighton/370-western-ave.html" data-ya-track="links_directory">Brighton</a>,
<a class="c-directory-list-content-item-link" href="ma/brookline/1717-beacon-st.html" data-ya-track="links_directory">Brookline</a>,
<a class="c-directory-list-content-item-link" href="ma/chestnut-hill/1-boylston-st.html" data-ya-track="links_directory">Chestnut Hill</a>,
<a class="c-directory-list-content-item-link" href="ma/dedham/795-providence-hwy.html" data-ya-track="links_directory">Dedham</a>,
<a class="c-directory-list-content-item-link" href="ma/marshfield/1-snow-rd.html" data-ya-track="links_directory">Marshfield</a>,
<a class="c-directory-list-content-item-link" href="ma/newtonville/33-austin-st.html" data-ya-track="links_directory">Newtonville</a>,
<a class="c-directory-list-content-item-link" href="ma/quincy/130-granite-st.html" data-ya-track="links_directory">Quincy</a>,
<a class="c-directory-list-content-item-link" href="ma/waltham/1070-lexington-st.html" data-ya-track="links_directory">Waltham</a>,
<a class="c-directory-list-content-item-link" href="ma/west-roxbury/75-spring-st.html" data-ya-track="links_directory">West Roxbury</a>,
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/boston/1065-commonwealth-ave.html",
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/boston/33-kilmarnock-st.html",
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/boston/53-huntington-ave.html", 
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/cambridge/49-white-st.html",
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/cambridge/699-mt-auburn-st.html", 
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/dorchester/4-river-st.html",
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/dorchester/45-morrissey-blvd.html", 
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/somerville/14-mcgrath-hwy.html",
<div class="Teaser-content"><h2 class="Teaser-name"><a class="Teaser-nameLink" href="../ma/somerville/275-beacon-st.html".
'''

# parsing
soup = BeautifulSoup(html, 'html.parser')


# write to csv
with open('Star_Market.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Street', 'City']
    csv_writer.writerow(headers)


# extraction of html
    for a in soup.find_all('a', href=True):
        Street = a['href'].split('/')[-1].replace('.html', '').replace('-', ' ')
        City = a['href'].split('/')[-2].replace('-', ' ')
        csv_writer.writerow([Street, City])
 
    
