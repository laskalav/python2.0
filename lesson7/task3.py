# import yaml
# from pprint import pprint
#
# with open('config.yml') as f:
#     templates = yaml.safe_load(f)
#
# pprint(templates)

"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
 Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
что html-файлы расположены в родительских папках (они играют роль пространств имён);
 предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
 |--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
"""
import os
import shutil
hierarchy = {'project': [
        {'settings': [
            '__init__.py',
            'dev.py',
            'prod.py']},
        {'mainapp': [
            '__init__.py',
            'models.py',
            'views.py',
            {'templates': [
                {'mainapp': [
                    'base.html',
                    'index.html']}]}]},
        {'authapp': [
            '__init__.py',
            'models.py',
            'views.py',
            {'templates': [
                {'authapp': [
                    'base.html',
                    'index.html']}]}]}]}


