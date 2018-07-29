[![](https://travis-ci.com/LordOfPolls/Rule34-API-Wrapper.svg?branch=master)](https://travis-ci.com/LordOfPolls/Rule34-API-Wrapper)
[![](https://codecov.io/gh/LordOfPolls/Rule34-API-Wrapper/branch/master/graph/badge.svg)](https://codecov.io/gh/LordOfPolls/Rule34-API-Wrapper)
[![](http://pepy.tech/badge/rule34)](http://pepy.tech/project/rule34)
![](https://img.shields.io/pypi/pyversions/rule34.svg)
![](https://img.shields.io/pypi/v/rule34.svg)
![](https://img.shields.io/github/issues-raw/LordOfPolls/Rule34-API-Wrapper.svg)
# Rule34.xxx API Wrapper

This is a simple module for simplifying access to the rule34.xxx API asynchronously

To assist bot developers, this wrapper doesnt use ``requests`` at all. Instead it uses aiohttp and coroutines. 

### If you arent coding asynchronously, simply use these lines when using this api:
```python
import asyncio #allows you to call the coroutine
import rule34
loop = asyncio.get_event_loop() # create an async event loop
rule34 = rule34.Rule34(loop) # call rule34 and give pass the event loop
# and then when calling the wrapper, use this
data = loop.run_until_complete(rule34.getImageURLS("SearchQuery"))
```
An update is coming to simplify this
### If you are coding asynchronously use this:
```python
import asyncio
import rule34
rule34 = rule34.Rule34([your event loop])
# and then when calling the wrapper, use this
await rule34.getImageURLS("SearchQuery")
```
# How do i install this?  
### From Pypi:  
``pip install rule34``
### From github
``pip install https://github.com/LordOfPolls/Rule34-API-Wrapper/archive/master.zip --upgrade ``

# Want to help improve the wrapper?
Sure! Just make a pull request ^-^

If your change improves how the wrapper works, ill merge it!

I advise you dont modify ``.travis.yml`` or the function ``selfTest``, because theyre used by travis-ci and modifying them may cause the build to fail when testing

# What to do if it stops working
1. Scream and panic at your lost porn
2. Breathe
2. [Make an issue on github](https://github.com/LordOfPolls/Rule34-API-Wrapper/issues/new), and be as detailed as possible
(screenshots and tracebacks help a lot)
# How do i use it?  
Each function has a docstring that explains what it is, and what arguments it needs, ill go over them simply here  
- ``urlGen(tags, limit, id, PID, deleted)``  
  - Generates a URL based on arguments which is used to obtain an XML document  

| Argument      | Purpose                          |Usage                      | Type  |
| ------------- |:--------------------------------:|:-------------------------:|:-----:|
| tags          |A search term                     |`urlGen(tags="furry")`     |str/int|
| limit         |A limit of how many posts you want|`urlGen([args],limit=100)` |str/int|
| id            |An Id of the post                 |`urlGen(id=12312)`         |str/int|
| PID           |Page number of the search         |`urlGen([args],PID=2`      |str/int|
| deleted       |Adds deleted posts to your search |`urlGen(deleted=True`      |bool   |

- ``totalImages(tags)``  
  - returns an int of how many posts match a tag  
  
| Argument      | Purpose                          |Usage                      | Type  |
| ------------- |:--------------------------------:|:-------------------------:|:-----:|
|tags           |A search term                     |`totalImages("furry")`     |str    |

- ``getImageURLS(tags)``  
  - returns a list of urls for every post's image/webm/gif
  
| Argument      | Purpose                          |Usage                      | Type  |
| ------------- |:--------------------------------:|:-------------------------:|:-----:|
|tags           |A search term                     |`getImageURLS(tags)`       |str    |
|fuzzy          |Toggles fuzzy searching           |`getImageURLS(fuzzy=True)` |bool   |
|randomPID      |Randomises the PID when singlePage is on|`getImageURLS(randomPID=True)`|bool|
|singlePage     |Limits search to one page (100 images)|`getImageURLS(singlePage=True`|bool|
|OverridePID    |Allows you to choose a PID        |`getImageURLS(OverridePID=1)`|int|

- ``getPostData(PostID)``
  - returns a dictionary of information about a post
  
| Argument      | Purpose                          |Usage                      | Type  |
| ------------- |:--------------------------------:|:-------------------------:|:-----:|
|PostID         |The ID of a post                  |`getPostData(12345)`       |str/int|


