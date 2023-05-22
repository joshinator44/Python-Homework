#!/usr/bin/env python3
from urllib import request, parse
import json
import ssl
from objects import Category, Meal

ssl._create_default_https_context = ssl._create_unverified_context


def get_categories():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?c=list'
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except(ValueError, KeyError, TypeError):
        print("JSON format error")

    return categories

