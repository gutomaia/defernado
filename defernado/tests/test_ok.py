import unittest
from tornado.testing import AsyncHTTPTestCase, gen_test
from tornado.web import Application

# from tornado.ioloop import IOLoop
from defernado.web import MainHandler, defer
import asyncio


class TestMainHandler(AsyncHTTPTestCase):
    def get_app(self):
        return Application(
            [
                (r'/process', MainHandler),
            ]
        )

    def test_get_request(self):
        # Test that the handler responds correctly
        response = self.fetch('/process', method='GET')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body.decode(), 'Request processed!!!')

    @gen_test
    async def test_defer_function(self):
        # This variable will help us confirm the deferred function ran
        self.execution_log = []

        # Sample deferred functions
        def mock_task(arg, kwarg1=None):
            self.execution_log.append(
                f'mock_task executed with {arg}, {kwarg1}'
            )

        def another_mock_task(arg, kwarg2=None):
            self.execution_log.append(
                f'another_mock_task executed with {arg}, {kwarg2}'
            )

        # Defer the tasks
        defer(mock_task, '1', kwarg1='2')
        defer(another_mock_task, '3', kwarg2='4')

        # Await a short timeout to let deferred tasks execute
        # await IOLoop.current().add_timeout(
        #     "herro",
        #     IOLoop.current().time() + 0.1,
        #     lambda *args: None)
        await asyncio.sleep(0.1)

        # Check that deferred tasks were executed
        self.assertIn('mock_task executed with 1, 2', self.execution_log)
        self.assertIn(
            'another_mock_task executed with 3, 4', self.execution_log
        )


if __name__ == '__main__':
    unittest.main()
