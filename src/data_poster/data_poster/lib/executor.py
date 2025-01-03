import concurrent.futures


executor = None


def get_global_executor():
    global executor
    if executor is None:
        executor = concurrent.futures.ThreadPoolExecutor()
    return executor
