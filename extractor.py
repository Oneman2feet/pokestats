from bs4 import BeautifulSoup
import urllib2,html5lib
import re

def loadSite(name):
    try:
        return BeautifulSoup(urllib2.urlopen("http://bulbapedia.bulbagarden.net/wiki/"+name+"_%28Pok%C3%A9mon%29").read(),"html5lib").find(id="mw-content-text")
    except:
        return False

def getInfo(name):
    site = loadSite(name)

    if (site==False):
        return None

    info = []
    info.append(getTypes(site))
    info.append(getStats(site))
    info.append(getLocs(site))
    info.append(getType(site))
    info.append(getEVs(site))
    info.append(getCatchRate(site))
    info.append(getEvolutions(site))
    info.append(getAbilities(site))
    return info

def getTypes(site):

    types = site.find(text=re.compile('Under normal battle conditions in Generation VI*'))
    types = types.parent.parent.parent.parent.parent.parent.parent.parent.parent
    return removeLinks(types)

def getStats(site):
    stats = site.find(href="/wiki/Stats",title="Stats").parent.parent.parent.parent
    return removeLinks(stats)

def getLocs(site):
    locs = site.find_all("small",text="Generation V")[1].parent.parent.parent.parent
    return removeLinks(locs)

def getType(site):
    myType = site.find("a",title="Type").parent.parent.parent
    return removeLinks(myType)

def getEVs(site):
    EVs = site.find("a",title=re.compile("List of Pok.mon by effort value yield")).parent.parent.parent
    return removeLinks(EVs)

def getCatchRate(site):
    catchRate = site.find("a",title="Catch rate").parent.parent
    return removeLinks(catchRate)

def getEvolutions(site):
    evolutions = site.find_all("p",limit=2)[1]
    return filterLinks(evolutions)

def getAbilities(site):
    abilities = site.find("a",title="Ability").parent.parent.parent
    return removeLinks(removeTables(abilities))

def filterLinks(html):
    for tag in html.find_all("a"):
        if not ("(Pok%C3%A9mon)" in str(tag['href'])):
            tag.unwrap()
        else:
            tag['href'] = tag['href'].replace('/wiki','').replace('_(Pok%C3%A9mon)','')
    return html

def removeLinks(html):
    i = len(html.find_all("a"))
    for x in xrange(0,i):
        html.find("a").unwrap()
    return html

def removeTables(html):
    for tag in html.find_all(style="display:none;"):
        tag.decompose()
    for tag in html.find_all("td",class_="roundy"):
        tag.unwrap()
    for tag in html.find_all("br"):
        tag.unwrap()
    for tag in html.find_all("td"):
        tag.name="li"
    for tag in html.find_all("small"):
        tag.contents = "(" + str(tag.contents[0]).strip() + ")"
        tag.unwrap()
    return html










