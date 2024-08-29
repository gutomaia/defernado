import tornado.ioloop
import tornado.web
from utils import defer
import asyncio


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Request processed!')
        print('here1')
        defer(self.some_background_task, 'arg1', kwarg1='value1')
        defer(self.another_background_task, 'arg2', kwarg2='value2')
        print('here2')
        self.write('!!')
        self.finish()

    async def some_background_task(self, arg, kwarg1=None):
        # Background task logic
        await asyncio.sleep(10)  # Delay for 1 second
        print(f'Executing some background task with {arg}, {kwarg1}')

    def another_background_task(self, arg, kwarg2=None):
        # Another background task logic
        print(f'Executing another background task with {arg}, {kwarg2}')


def make_app():
    return tornado.web.Application(
        [
            (r'/process', MainHandler),
        ]
    )
