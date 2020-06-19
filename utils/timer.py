#! /usr/bin/env python
"""
Just some classes that help benchmark execution speed.

Timer    : A context manager
AutoTimer: A self-adjusting timer. It replicates the behavior of the timeit module.

"""
import gc
import timeit
import typing

__all__ = ["Timer"]


def format_timing(timing: float, number_of_loops: int = 1) -> typing.Tuple[float, str]:
    """
    Return timing + unit

    Input
    =====

    timing         : The timing in seconds.
    number_of_loops: The number of loops that were required to get this timing value.
                     It defaults to 1.

    """
    usec = timing * 1e6 / number_of_loops
    if usec < 1000:
        return usec, "usec"
    msec = usec / 1000
    if msec < 1000:
        return msec, "msec"
    return timing, "sec"


class Timer:  # pylint: disable=too-many-instance-attributes, attribute-defined-outside-init
    """
    A context manager that can be used to benchmark blocks of code (function calls etc).

    Usage
    =====

    It should be used to code blocks of code that take "significant" time to be executed
    (e.g. milli-seconds). It is not suitable for micro-benchmarks because it introduces
    some overhead.

    Example
    =======

        >>> with Timer() as t:
        >>>     # whatever ...

    See also
    ========

    Something like this may end up in the Standard library: http://bugs.python.org/issue19495

    """

    def __init__(
        self,
        msg: str = "",
        log_func: typing.Optional[typing.Callable[..., None]] = None,
        disable_gc: bool = True,
        precision: int = 3,
    ) -> None:
        self.log_func = log_func
        self.msg = "Executed '%s' in:" % msg if msg else "Executed in:"
        self.msg += " %.*g %s"
        self.disable_gc = disable_gc
        self.precision = precision
        self.timer = timeit.default_timer
        # self.start = self.end = self.interval = None
        # self.gc_state = None
        # self.seconds = None
        # self.interval = None
        # self.unit = None

    def __enter__(self) -> "Timer":
        if self.disable_gc:
            self.gc_state = gc.isenabled()
            gc.disable()
        self.start = self.timer()
        return self

    def __exit__(self, *args: typing.List[typing.Any]) -> None:
        self.end = self.timer()
        if self.disable_gc and self.gc_state:
            gc.enable()

        self.seconds = self.end - self.start
        self.interval, self.unit = format_timing(self.seconds)
        if self.log_func is not None:
            self.log_func(self.msg, self.precision, self.interval, self.unit)
        else:
            print(self.msg % (self.precision, self.interval, self.unit))
