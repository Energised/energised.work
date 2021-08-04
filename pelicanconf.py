#!/usr/bin/env python
# @author Dan Woolsey
# -*- coding: utf-8 -*- #

AUTHOR = 'dan woolsey'
SITENAME = 'energised.work'
SITEURL = 'https://energised.work'

SITETITLE = AUTHOR
SITESUBTITLE = "take me back to the 80's"

PATH = "content"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('pumpy', 'https://github.com/Energised/Pumpy'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/daniel-woolsey-104558109/'),
          ('github', 'https://github.com/Energised'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme settings
THEME = "Flex"
SITELOGO = "/images/profile.png"
FAVICON = "/images/favicon.png"

MAIN_MENU = True
MENUITEMS = (("Posts", ""),("Categories", ""),)


PLUGIN_PATHS = ["plugins"]

PLUGINS = ["i18n_subsites"]
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

I18N_TEMPLATES_LANG = "en"

STATIC_PATHS = ["images"]
