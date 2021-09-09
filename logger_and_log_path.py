import datetime


def set_log_path(log_path):
    def logger(some_func):
        log_str = ''

        def new_some_func(*args, **kwargs):
            with open(log_path, 'a', encoding='utf-8') as logfile:
                nonlocal log_str
                log_str = f'{datetime.datetime.now()} : '
                log_str += f'функция <{some_func.__name__}>'
                log_str += f', аргументы *args: <{args}>, **kwargs: <{kwargs}>'
                result = some_func(*args, **kwargs)
                log_str += f'- возвращаемое значение <{result}>'
                logfile.write(f'{log_str}\n')
                return result

        return new_some_func

    return logger
