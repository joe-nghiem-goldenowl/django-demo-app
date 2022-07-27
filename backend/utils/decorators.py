import bugsnag
def track_bugs(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            bugsnag.notify(e)
    return wrapper
