# import sys 
# import logging
# from src.logger import logging


# def error_message_details(error, error_detail:sys):
#     _,_,exc_tb = error_detail.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     error_message = "Error occured in Python Script name [{0}] line number [{1}] error message [{2}]".format(
#         file_name, exc_tb.tb_lineno, str(error)      
#         )
    
#     return error_message

# class CustomException(Exception):
#     def __init__(self, error_message, error_details:sys):
#         super().__init__(error_message)
#         self.error_message = error_message_details(error_message, error_detail=error_details)

#     def __str__(self):
#         return self.error_message
    

# import sys

# def error_message_detail(error: Exception, error_details: sys):
#     _,_,exc_tb = error_details.exc_info()

#     file_name = exc_tb.tb_frame.f_code.co_filename
#     line_number = exc_tb.tb_lineno

#     error_message = (
#         f"Error occured in the file {file_name}"
#         f"at line-number {line_number}"
#         f"with message -- {str(error)}"
#     )
#     return error_message


# class CustomException(Exception):
#     def __init__(self, error: Exception, error_details: sys):
#         super().__init__(str(error))
#         self.error_message = error_message_detail(error, error_details)

#     def __str__(self):
#         return self.error_message



import sys

def error_message_details(error: Exception, error_details: sys):
    _,_,exc_tb = error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_message = (
        f"The error occured in file -- {file_name} \n"
        f"error line is -- {line_no} \n"
        f"error message is -- {str(error)}"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error: Exception, error_details: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_details)

    def __str__(self):
        return self.error_message