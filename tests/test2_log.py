__author__ = 'gareth ng'

from loggly.log import Log

log = Log.get_logger(__name__)


class Test2(object):

    def __init__(self):
        log.debug(msg="this is a test for loggly", uuid="2b24bad1c5df6b4551768fe09ae877b893fc35505847e80f119c395bca27", elapsed=256)


if __name__ == "__main__":
    Test2()