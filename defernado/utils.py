from tornado.ioloop import IOLoop


def defer(func, *args, **kwargs):
    """
    Schedules a function to be executed in the background after the response is
    sent.

    Args:
        func: The callable to be executed.
        *args: Positional arguments for the callable.
        **kwargs: Keyword arguments for the callable.
    """
    # Add the function to the IOLoop to run it asynchronously
    IOLoop.current().add_callback(func, *args, **kwargs)
