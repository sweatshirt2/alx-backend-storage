#!/usr/bin/env python3
"""
This module provides a redis Cache class to store data and get the stored data key
"""


import redis
from uuid import uuid4


class Cache:
  """
  A class to interface with Redis for convenient interaction
  """

  def __init__(self):
    """
    Initialize the redis instance and flush the db
    """
    self._redis = redis.Redis()
    self._redis.flushdb()


  def store(self, data) -> str:
    """
    Stores data with a unique key and returns the key
    
    Args:
      data: The data to be stored in the cache

    Returns:
      str: the key of the stored data
    """
    
    # generate the key with an instance variable from the same object
    key = self.generate_key()
    # use the key to store the data
    self._redis.set(key, data)

    # return the key
    return key

  def generate_key(self) -> str:
    # generate and return a uuid-v4 key
    return str(uuid4())
