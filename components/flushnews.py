# -*- coding: utf-8 -*-
from meya import Component


class HelloWorld(Component):

    def start(self):
        # reset content refresh time stamp
        self.db.bot.set('content_refresh_ts', 0)
        # flush the content database
        content_list = self.db.table('content').filter()
        for content in content_list:
            self.db.table('content').delete(content["id"])
        return self.respond()
