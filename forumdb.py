# "Database code" for the DB Forum.

import datetime

POSTS = [("This is the first post.", "This is my first description", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  return reversed(POSTS)

def add_post(content, description):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, description, datetime.datetime.now()))


