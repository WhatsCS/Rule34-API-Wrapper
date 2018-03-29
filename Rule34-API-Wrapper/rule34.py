from __future__ import print_function
from collections import defaultdict
from xml.etree import cElementTree as ET
import urllib.request
import time

class rule34Exception(Exception):
    """Rule34 rejected you"""
    def __init__(self, message, *args):
        self.message = message
        super(rule34Exception, self).__init__(message, *args)


def ParseXML(rawXML):
    ###Using https://stackoverflow.com/a/10077069###
    print(rawXML.items())
    if "Search error: API limited due to abuse" in str(rawXML.items()):
        raise rule34Exception('Rule34 rejected your request due to "API abuse"')

    d = {rawXML.tag: {} if rawXML.attrib else None}
    children = list(rawXML)
    if children:
        dd = defaultdict(list)
        for dc in map(ParseXML, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {rawXML.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if rawXML.attrib:
        d[rawXML.tag].update(('@' + k, v) for k, v in rawXML.attrib.items())
    if rawXML.text:
        text = rawXML.text.strip()
        if children or rawXML.attrib:
            if text:
              d[rawXML.tag]['#text'] = text
        else:
            d[rawXML.tag] = text
    return d

def urlGen(tags=None, limit=None, id=None, PID=None, **kwargs):
    """Generates a URL to access the api using your input:
    Arguments:
        "limit"||How many posts you want to retrieve
        "pid"  ||The page number.
        "tags" ||The tags to search for. Any tag combination that works on the web site will work here. This includes all the meta-tags. See cheatsheet for more information.
        "cid"  ||Change ID of the post. This is in Unix time so there are likely others with the same value if updated at the same time.
        "id"   ||The post id.
    If none of these arguments are passed, None will be returned
    """
    URL = "https://rule34.xxx/index.php?page=dapi&s=post&q=index"
    
    if PID != None:
        URL += "&pid={}".format(PID)
    if limit != None:
        URL += "&limit={}".format(limit)
    if id != None:
        id += "&id={}".format(id)
    if tags != None:
        tags = str(tags).replace(" ", "+")
        URL += "&tags={}".format(tags)
    if PID != None or limit != None or id != None or tags != None:
        return URL
    else:
        return None

def totalImages(tags):
    """Get an int of how many images are on rule34.xxx"""
    XMLData = urllib.request.urlopen(urlGen(tags)).read()
    XMLData = ET.XML(XMLData)
    XML = ParseXML(XMLData)
    return int(XML['posts']['@count'])

def getImageURLS(tags):
    """Returns a list of all images/webms/gifs it can find
    This function can take a LONG time to finish with huge tags. E.G. in my testing "gay" took 200seconds to finish (740 pages)"""
    
    imgList = []
    if totalImages(tags) != 0:
        PID = 0
        t = True
        imgList = []
        while t:
            tempURL = urlGen(tags=tags, PID=PID)
            XML = urllib.request.urlopen(tempURL).read() #<-- This line is what causes this function to take as long as it does

            XML = ParseXML(ET.XML(XML))

            if len(imgList) >= int(XML['posts']['@count']): #"if we're out of images to process"
                t = False #"end the loop"
            else:
                for data in XML['posts']['post']:
                    imgList.append(str(data['@file_url']))
            PID += 1
        return imgList
    else:
        return None

def getPostData(PostID):
    """"Unfinished function"""
    return
    url = urlGen(PID=str(PostID))
    print(url)
    XML = urllib.request.urlopen(url).read()
    XML = ParseXML(ET.XML(XML))