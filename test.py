from src.logger import logger
from src.exception import CustomException
import sys

def divide_numbers(a,b):
    return a/b

try:
    divide_numbers(1,0)
except Exception as e:
    custom_error = CustomException(e, sys)
    logger.error(
        f"An error has occured \n"
        f"{custom_error}"
        )
    raise custom_error
    
    