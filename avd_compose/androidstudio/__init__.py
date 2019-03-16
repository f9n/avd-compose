import os
import sys
import functools


class AndroidHome:
    @staticmethod
    def get():
        return os.getenv("ANDROID_HOME")

    @staticmethod
    def check():
        path = AndroidHome.get()
        if path is None:
            sys.exit("The 'AndroidHome' environment variable is not defined.")

    @staticmethod
    def required(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            AndroidHome.check()
            return func(*args, **kwargs)

        return wrapper_decorator


class Tools:
    defaults = {
        "avdmanager": "Sdk/tools/bin/avdmanager",
        "sdkmanager": "Sdk/tools/bin/sdkmanager",
        "emulator": "Sdk/tools/emulator",
    }

    @staticmethod
    def get_full_path(name):
        return os.path.join(AndroidHome.get(), Tools.defaults[name])

