"""
Author: Gareth Ng
Email: wu.qingzhe@outlook.com
"""

import socket
import logging
import six


class CommonAdapter(logging.LoggerAdapter):
    """
    CommonAdapter
    """
    extra_field = ['uuid', 'elapsed']

    def __init__(self, logger, uuid=None, elapsed=None):
        self.uuid = uuid
        self.elapsed = elapsed
        extra = {
            'hostname': socket.gethostname()
        }
        super().__init__(logger, extra)

    def __format_extra(self, kwargs):
        kwargs_tmp = dict(kwargs)
        log_fields = kwargs_tmp.keys()
        # fill empty field
        for key in CommonAdapter.extra_field:
            if key not in log_fields:
                if key == "uuid" and isinstance(self.uuid, six.string_types) and len(self.uuid) > 0:
                    kwargs['uuid'] = self.uuid
                elif key == "elapsed" and isinstance(self.elapsed, six.string_types) and len(self.elapsed) > 0:
                    kwargs["elapsed"] = self.elapsed
                else:
                    kwargs[key] = None
        # filter not valid field
        for field in log_fields:
            if field not in CommonAdapter.extra_field:
                del kwargs[field]

    def process(self, msg, kwargs):
        self.__format_extra(kwargs)
        extra_pack = {'extra': kwargs}
        extra_pack['extra'].update(self.extra)
        return msg, extra_pack


class Log:

    logger = None

    @staticmethod
    def get_logger(name, uuid=None, elapsed=None):
        if not isinstance(name, six.string_types):
            raise TypeError('A logger name must be string or Unicode')
        if isinstance(name, six.string_types):
            name = f"logpilot-{name}"

        # configure logging
        log_t = logging.getLogger(name)
        log_t.propagate = False
        if not log_t.handlers:
            handler = logging.StreamHandler()
            log_fmt = ("%(asctime)s.%(msecs)03d|%(levelname)s|%(name)s|%(filename)s|%(lineno)d|%(module)s|%(funcName)s|"
                       "%(processName)s|%(threadName)s|%(message)s|%(hostname)s|%(uuid)s|%(elapsed)s")
            date_fmt = '%Y-%m-%d %H:%M:%S'
            formatter = logging.Formatter(fmt=log_fmt, datefmt=date_fmt)
            handler.setFormatter(formatter)
            log_t.addHandler(handler)
        log_t.setLevel(logging.INFO)
        Log.logger = CommonAdapter(log_t, uuid, elapsed)
        return Log.logger

    @staticmethod
    def remove_logger():
        Log.logger = None
