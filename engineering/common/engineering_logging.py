import logging
from common import config

logging.basicConfig(filename=config.CONF.log_file, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )

def log_for_func_of_class(logger_name):
    def _log_wrapper(func):
        def __log_wrapper(class_self):
            logger = logging.getLogger(logger_name)
            start_info = 'Start to execute %s' % getattr(func, '__name__')
            logger.info(start_info)
            print(start_info)

            result = func(class_self)

            end_info = 'End to execute %s, result is: %s' % (getattr(func, '__name__'), result)
            logger.info(end_info)
            print(end_info)
            return result

        return __log_wrapper
    return _log_wrapper

def log_for_func_args_of_class(logger_name, *args):
    def _log_wrapper(func):
        def __log_wrapper(class_self):
            logger = logging.getLogger(logger_name)
            start_info = 'Start to execute %s' % getattr(func, '__name__')
            logger.info(start_info)
            print(start_info)

            result = func(class_self, *args)

            end_info = 'End to execute %s, result is: %s' % (getattr(func, '__name__'), result)
            logger.info(end_info)
            print(end_info)
            return result

        return __log_wrapper
    return _log_wrapper