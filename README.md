<!-- I'll figure out this shit later lmao
[![Build Status](https://travis-ci.com/LordOfPolls/Rule34-API-Wrapper.svg?branch=master)](https://travis-ci.com/LordOfPolls/Rule34-API-Wrapper) -->
[![Test Coverage](https://codecov.io/gh/LordOfPolls/Rule34-API-Wrapper/branch/master/graph/badge.svg)](https://codecov.io/gh/LordOfPolls/Rule34-API-Wrapper)
<!-- [![Downloads](https://static.pepy.tech/personalized-badge/rule34?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/rule34) -->
<!-- ![Supported Versions](https://img.shields.io/pypi/pyversions/rule34.svg) -->
<!-- ![Latest Version](https://img.shields.io/pypi/v/rule34.svg) -->
<!-- ![Open Issues](https://img.shields.io/github/issues-raw/LordOfPolls/Rule34-API-Wrapper.svg) -->
# Rule34.xxx API Wrapper

First off, thank you to LordOfPolls along with the many other's that have forked the original.

This is a simple module for simplifying access to the rule34.xxx API asynchronously

To assist bot developers, this wrapper doesnt use ``requests`` at all. Instead it uses aiohttp. And to assist people who arent coding asynchronously, theres a class called ``Sync`` that allows this module to work without worrying about coroutines. 

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

# How do I install this?  
<!-- ### From Pypi:  
``pip install rule34`` -->
### From github
``pip install https://github.com/WhatsCS/Rule34-API-Wrapper/archive/master.zip --upgrade ``

# Want to help improve the wrapper?
Sure! Just make a pull request ^-^

If your change improves how the wrapper works, I'll merge it!

# What to do if it stops working
1. Scream and panic at your lost porn
2. Breathe
2. [Make an issue on github](https://github.com/WhatsCS/Rule34-API-Wrapper/issues/new), and be as detailed as possible
(screenshots and tracebacks help a lot)

