import scrapbox

import filecmp
import os
from unittest import TestCase
from nose.tools import eq_, ok_

class PagesTestCase(TestCase):
    client = scrapbox.Client()

    # /api/pages/:projectName
    def test_page_list(self):
        project = self.client.get("/pages/Growingforadream", skip=3, limit=10)

        eq_(project["count"], 5)
        eq_(project["skip"], 3)
        eq_(project["limit"], 10)


    # /api/pages/:projectName/:pageTitle
    def test_page(self):
        page = self.client.get("/pages/Growingforadream/Scrapbox_API_Wrapper")

        eq_(page["title"], "Scrapbox API Wrapper")
        eq_(page["descriptions"][0], 'ほげほげほげほげ。')


    # /api/pages/:projectName/:pageTitle/text
    def test_page_text(self):
        text = self.client.get("/pages/Growingforadream/アイカツ！/text")

        eq_(text, "アイカツ！\nアイドル活動")


    # /api/pages/:projectName/:pageTitle/icon
    def test_page_icon(self):
        icon = self.client.get("/pages/Growingforadream/HelloRusk/icon")

        with open("dump_image.jpg", "wb") as f:
            f.write(icon)

        ok_(filecmp.cmp("dump_image.jpg", "test_image.jpg"))
        os.remove("dump_image.jpg")