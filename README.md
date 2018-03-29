# Rule34.xxx API Wrapper

This is a simple module for simplifying access to the rule34.xxx API

# How do i install this?  
### Via pip:  
``pip install rule34``

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

- ``getPostData(PostID)``
  - returns a dictionary of information about a post
  
| Argument      | Purpose                          |Usage                      | Type  |
| ------------- |:--------------------------------:|:-------------------------:|:-----:|
|PostID         |The ID of a post                  |`getPostData(12345)`       |str/int|
