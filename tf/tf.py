import functools
import timeit
import typing

available_formats = ('ms', 'sec', 'min', 'hr')


def tf(func: typing.Optional[typing.Callable] = None, *, precision: int = 3, time_format: str = "ms") -> typing.Callable:
    if precision < 0:
        raise ValueError('Precision must be greater than 0')
    if time_format not in available_formats:
        print(time_format)
        raise ValueError(f"""Time format must be one of these arguments: {
                         ", ".join(available_formats)}""")
    if func is None:
        return functools.partial(tf, precision=precision, time_format=time_format)

    @functools.wraps(func)
    def decorated(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time

        match time_format.lower():
            case "ms":
                elapsed_time *= 1000
                unit = "ms"
            case "min":
                elapsed_time /= 60
                unit = "min"
            case "hr":
                elapsed_time /= 3600
                unit = "hr"
            case _:
                unit = "sec"

        print(f"""Function '{func.__name__}' executed in {
              elapsed_time:.{precision}f} {unit}""")
        return result

    return decorated
