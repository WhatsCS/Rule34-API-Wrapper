class Rule34Post:
    """
    The data structure for images on rule34. By default, all items are none,
    they will only be something else if rule34.xxx specifies a value.

    if ``initialised`` is False, that means somehow this object wasn't initialised properly, and you should discard it
    """
    initialised = False  # If this is false, the post data isn't complete for whatever reason, dont use it

    # The image's data
    height = None  # Image dimension height
    width = None  # Image dimension width
    score = None  # The image's user determined rating
    file_url = None  # The image URL
    parent_id = None  # If this post is a child, this will show the ID of its parent
    has_children = None  # Is this post a parent?
    has_comments = None  # Are there comments on this post?
    has_notes = None  # Are there notes on this post?
    created_at = None  # When the post was posted, funnily enough
    change = None  # Not sure what this is used for, but all posts have it. If you know, leave an issue telling me
    md5 = None  # The MD5 hash of the post, i have no idea why its necessary to expose, but rule34.xxx generates it
    creator_ID = None  # The post author's ID
    rating = None  # The rating of the post, pretty much always "e", ie Explicit

    # SAMPLE VERSION - These are smaller images, saving some data, if necessary
    sample_url = None  # Sample Image URL
    sample_height = None  # Sample image dimension height
    sample_width = None  # Sample image dimension width

    # PREVIEW VERSION - A TINY version of the image, suitable for thumbnails
    preview_url = None  # Preview image URL
    preview_height = None  # Preview image height
    preview_width = None  # Preview image width


