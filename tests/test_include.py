# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

from helper import verify_conversion

def test_include():
    verify_conversion(
        '''
``` {include="tests/lorem"}
```
        ''',
        '''
``` {include="tests/lorem"}
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Duis pretium rutrum dignissim.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
Interdum et malesuada fames ac ante ipsum primis in faucibus.
Ut iaculis arcu sed dui ornare pretium.
```
        '''
    )

def test_include_start_from():
    verify_conversion(
        '''
``` {include="tests/lorem" startFrom="2"}
```
        ''',
        '''
``` {include="tests/lorem" startFrom="2"}
Duis pretium rutrum dignissim.
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
Interdum et malesuada fames ac ante ipsum primis in faucibus.
Ut iaculis arcu sed dui ornare pretium.
```
        '''
    )

def test_include_end_at():
    verify_conversion(
        '''
``` {include="tests/lorem" endAt="2"}
```
        ''',
        '''
``` {include="tests/lorem" endAt="2"}
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Duis pretium rutrum dignissim.
```
        '''
    )

def test_include_latex():
    verify_conversion(
        '''
``` {include="tests/lorem" startFrom="1" endAt="2"}
```
        ''',
        '''
``` {startFrom="1"}
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Duis pretium rutrum dignissim.
```
        ''',
        format='latex'
    )

def test_error():
    verify_conversion(
        '''
``` {include="tests/unexisting" startFrom="a" endAt="a"}
```
        ''',
        '''
``` {include="tests/unexisting" startFrom="a" endAt="a"}
```
        '''
    )

