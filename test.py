#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:02:36 2018

@author: Arina
"""

from newspaper import Article
from keywords import author, test_url

def test_article():
    """Test if the author of the article located at the test_url 
    is correctly parsed."""
    article = Article(test_url)
    article.download()
    article.parse()
    assert author in article.authors

test_article()