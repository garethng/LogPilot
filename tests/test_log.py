__author__ = 'gareth ng'


from loggly.log import Log
import logging
log = Log.get_logger('test2222')
log.logger.setLevel(logging.DEBUG)

class Test(object):

    def __init__(self):
        log.info(msg="this is a test loggly", hahah='hooooo.', age=10000, fake_key='not valid')


if __name__ == '__main__':
    from loggly.log import Log
    ilog = Log.get_logger("test3")
    a = Test()
    ilog.info(msg="this is a test loggly", hahah='hooooo.', uuid="1234567890")
