import functools
import timeit
import typing


class tf:
    available_formats: tuple = ("ms", "sec", "min", "hr")

    def __init__(self, precision: int = 3, time_format: str = "ms"):
        if precision < 0:
            raise ValueError("Precision must be greater than 0")
        if time_format not in self.available_formats:
            raise ValueError(
                f"Time format must be one of these arguments: {', '.join(self.available_formats)}"
            )
        self.precision = precision
        self.time_format = time_format

    def __call__(
        self, func: typing.Optional[typing.Callable] = None
    ) -> typing.Callable:
        if func is None:
            return functools.partial(self.__call__)

        @functools.wraps(func)
        def decorated(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            start_time = timeit.default_timer()
            result = func(*args, **kwargs)
            end_time = timeit.default_timer()
            elapsed_time = end_time - start_time

            match self.time_format.lower():
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

            print(
                f"Function '{func.__name__}' executed in {elapsed_time:.{self.precision}f} {unit}"
            )
            return result

        return decorated
