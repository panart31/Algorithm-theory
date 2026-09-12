import importlib.util
import os


folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_task(filename):
    path = os.path.join(folder, filename)
    spec = importlib.util.spec_from_file_location(filename[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
