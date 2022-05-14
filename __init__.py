from types import ModuleType
from typing import Dict, Any, List



class NewAttr(object):
    """
    used instead of a NoneType in `__setattr__` and `_write_attr` so we can seperate `None` values, and new attributes.
    """ 
    pass



class Writable:
    def __init__(self, module: ModuleType) -> None:
        self.module = module
        self._file = module.__file__
        self.sub: Dict[str, Any] = {}
        for x in dir(module):
            self.sub[x] = module.__dict__[x]


    def __getattribute__(self, name) -> Any:
        try:
            return object.__getattribute__(self, 'sub')[name]
        except (KeyError, AttributeError):
            try:
                return object.__getattribute__(self, name)
            except (KeyError, AttributeError):
                raise AttributeError()


    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, 'sub'):
            try:
                old_val = self.sub[name]
            except KeyError:
                old_val = NewAttr()
            self.sub[name] = value
            self._write_attr(name, value, old_val)
            return
        object.__setattr__(self, name, value)


    def _write_attr(self, name, value, old_value) -> None:
        if isinstance(old_value, NewAttr):
            with open(self._file, 'r') as f:
                text: List[str] = f.readlines()
            text.append(f"{name} = {value}\n")
            with open(self._file, 'w') as f:
                f.writelines(text)
        else:
            with open(self._file, 'r') as f:
                text: List[str] = f.readlines()
            for line in text:
                if f"{name} = {old_value}" in line:
                    text[text.index(line)] = line.replace(f"{name} = {old_value}", f"{name} = {value}")
            with open(self._file, 'w') as f:
                f.writelines(text)