The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

------------------------------------------------------------------------

Days:
-----
 - Day 1: string, print, range, input, list, dictionaries, sort, shallow & deep copy, zip, loops
 - Day 2: set, generators & iterators, classes, inheritance, exceptions, input, output, files, yield
 - Day 3: datetime, modules & packages, keywords, names and name spaces, string, formatting, sys, os, subprocess

Questions:
----------
XML (lxml), xUnit (PyTest), DB orm (sqlalchemy), UI (Qt), Django (Web framework)

Useful packages:
----------------
 - ElementTree (XML): http://docs.python.org/3/library/xml.etree.elementtree.html?highlight=elementtree
 - lxml: http://lxml.de
 - pytest: https://pypi.python.org/pypi/pytest | http://pytest.org/latest/
 - doctest: http://docs.python.org/2/library/doctest.html
 - python Qt: http://pyqt.sourceforge.net/Docs/PyQt5/
 - sqlalchemy ORM: http://www.sqlalchemy.org | http://docs.sqlalchemy.org/en/rel_0_9/
 - cython (C-extensions): http://cython.org
 - debugging: print function, pdb or with IDE (e.g. PyCharm)

Exercises:
----------
 - total of 17 exercise scripts
 - each exercise contains some sample code
 - firstday.py, secondday.py and thridday.py has all the information related

Execution:
----------
python <script>.py
python3 <script>.py

pip install <package>

Examples:
---------
python exercise1.py
python3 exercise11.py

pip install pytest

Some useful links:
------------------
- http://python-future.org
- https://github.com/PythonCharmers/python-future
- https://github.com/qspin
- http://www.python.org

python packages (management & installing)
- https://pypi.python.org/pypi/pip

ipython (nice looking interactive webpage to execute short python scripts
- http://ipython.org

anaconda (not really needed for python development)
- https://store.continuum.io/cshop/anaconda/

ui
- https://wiki.python.org/moin/PyQt

code style
- http://legacy.python.org/dev/peps/pep-0008/
- http://www.pylint.org


Some other stuff:
-----------------
- install pip on mac: sudo easy_install pip
- virtualenvwrapper: create multiple virtual environment
    http://stackoverflow.com/questions/10763440/how-to-install-python3-version-of-package-via-pip

Test example:
-------------
python kristof$ py.test
========================================= test session starts ==========================================
platform darwin -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
collected 2 items

test/test_func.py .F

=============================================== FAILURES ===============================================
____________________________________________ test_add_fail _____________________________________________

    def test_add_fail():
>       assert add(2, 1) == 4
E       assert 3 == 4
E        +  where 3 = add(2, 1)

test/test_func.py:10: AssertionError
================================== 1 failed, 1 passed in 0.04 seconds ==================================

Debugging (pdb):
----------------
--> pdb:
print(s.format(name='Kristof', amount=amount(234.56), date=d.strftime('%d, %b %Y')))
pdb.set_trace()
print(s.format(name='Mark', amount=amount(1290.56), date=d.strftime('%d, %b %Y')))
--> output:
> /Users/kristof/Work/python/exercise17.py(29)<module>()
-> print(s.format(name='Mark', amount=amount(1290.56), date=d.strftime('%d, %b %Y')))
(Pdb) amount
<function amount at 0x10069f3b0>
(Pdb) amount(23)
'€23.00'
(Pdb) amount(342)
'€342.00'