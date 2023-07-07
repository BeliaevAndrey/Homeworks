from time import time_ns as _tns
from datetime import datetime as _dt


def timer_dec(func):

    def wrapper(*args, **kwargs):
        start = _tns()
        result = func(*args, **kwargs)
        end = (_tns() - start) / 1e9

        report = f'{_dt.now()}\t-- function: {func.__name__};'
        if args and len(args) >= 2:
            report += (f' process type: {args[1]};'
                       f' link: {args[0]};')
        elif args and isinstance(args[0], list):
            report += f' amount of links {len(args[0])};'

        if func.__name__ == 'main':
            report += f' totally time taken: {end}'
        else:
            report += f' time taken: {end}'

        print(report)

        with open('download.log', 'a', encoding='utf-8') as log_file_out:
            log_file_out.write(report + '\n')

        return result
    return wrapper
