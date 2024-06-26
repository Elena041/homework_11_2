 from functools import wraps
 from typing import Any,Callable,Dict

 def log(file_name: str,None,None) -> Callable:
    """Декоратор, который логирует вызов функции и ее результат в файл или в консоль"""

