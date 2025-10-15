# Given a string of HTML code, remove the tags and return the plain text content.

# The input string will contain only valid HTML.
# HTML tags may be nested.
# Remove the tags and any attributes.
# For example, '<a href="#">Click here</a>' should return "Click here".

import re

def strip_tags(html):

    split = re.sub("<\/\s*([a-zA-Z0-9]+)(\s+[^>]*)*>|<\s*([a-zA-Z0-9]+)(\s+[^>]*)*>", "", html)

    return split