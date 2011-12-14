import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from models import Message
from utils import strip_quotes

        
class UtilsTest(TestCase):
    def test_strip_quotes(self):
        body = """nyan nyan nyan nyan nyan
        nyan nyan nyan nyan nyan

        nyan nyan nyan nyan nyan

        2011/10/28 Nyan Cat <nyan@nyan.cat>:
         > hey guys
        > sarete il 31 dicembre con Pascal a Firenze?
        > lo spero tanto, nel caso ditemi qualcosa...
        >
        >>>
        >
        >>
        >"""
        
        body_stripped = """nyan nyan nyan nyan nyan
nyan nyan nyan nyan nyan

nyan nyan nyan nyan nyan
"""
        
        self.assertEquals(body_stripped.strip(), strip_quotes(body).strip())
    def test_strip_quotes(self):
        body = "miao\r\n\r\n2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n> try\r\n>\r\n> 2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n>> repr\r\n>>\r\n>> 2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n>>> meow\r\n>>>\r\n>>> 2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n>>>> mhh?\r\n>>>>\r\n>>>>\r\n>>>> 2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n>>>>> nyancat\r\n>>>>>\r\n>>>>> 2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n>>>>>> hi there\r\n>>>>>>\r\n>>>>>>\r\n>>>>>> 2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n>>>>>>> fgfg\r\n>>>>>>>\r\n>>>>>>> 2011/12/13 Fabrizio Sestito <fabrizio@gidsy.com>:\r\n>>>>>>>> dfdfd\r\n>>>>>>>>\r\n>>>>>>>> On Tue, Dec 13, 2011 at 12:35 PM, Fabrizio Sestito <fabrizio@gidsy.com> wrote:\r\n>>>>>>>>> ciao\n"
        
        body_stripped = """miao


"""
        
        self.assertEquals(body_stripped.strip(), strip_quotes(body).strip())

