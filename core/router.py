import pkgutil
import importlib
from fastapi import APIRouter


def register_routes(router: APIRouter, module_name: str = 'controllers', attribute_name: str = 'router'):
    package = importlib.import_module(module_name)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__, f"{package.__name__}."):
        module = importlib.import_module(module_name)
        module_router = getattr(module, attribute_name, None)
        if router is not None and isinstance(module_router, APIRouter):
            router.include_router(module_router)