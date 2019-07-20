[![](https://travis-ci.com/LordOfPolls/Rule34-API-Wrapper.svg?branch=master)](https://travis-ci.com/LordOfPolls/Rule34-API-Wrapper)
[![](https://codecov.io/gh/LordOfPolls/Rule34-API-Wrapper/branch/master/graph/badge.svg)](https://codecov.io/gh/LordOfPolls/Rule34-API-Wrapper)
[![](http://pepy.tech/badge/rule34)](http://pepy.tech/project/rule34)
![](https://img.shields.io/pypi/pyversions/rule34.svg)
![](https://img.shields.io/pypi/v/rule34.svg)
![](https://img.shields.io/github/issues-raw/LordOfPolls/Rule34-API-Wrapper.svg)
# Rule34.xxx API Wrapper

This is a simple module for simplifying access to the rule34.xxx API asynchronously

To assist bot developers, this wrapper doesnt use ``requests`` at all. Instead it uses aiohttp. And to assist people who arent coding asynchronously, theres a class called ``Sync`` that allows this module to work without worrying about coroutines. 

# How do i use it?  
Documentation can be found in the wiki: https://github.com/LordOfPolls/Rule34-API-Wrapper/wiki

### If you arent coding asynchronously, simply use this code
```python
import rule34
rule34 = rule34.Sync()
rule34.getImages("SearchQuery")
```
### If you are coding asynchronously use this code:
```python
import rule34
rule34 = rule34.Rule34([your event loop])
await rule34.getImages("SearchQuery")
```

For an example use case see: [Rule34 Downloader](https://github.com/LordOfPolls/Rule34-Downloader)

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

# Like what I do?

Why not buy me a coffee? http://paypal.me/LordOfPolls
