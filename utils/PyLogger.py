from datetime import datetime
import inspect
import os
import textwrap
import urllib.parse  # For encoding spaces

class PyLogger:

    @staticmethod
    def logsData():
        return datetime.now()

    @staticmethod
    def get_caller_info():
        frame = inspect.stack()[2]  # Get caller's stack frame
        file_path = os.path.abspath(frame.filename)  # Get full file path
        file_path = urllib.parse.quote(file_path,  safe=":/\\")  # Encode spaces as %20
        line_number = frame.lineno  # Get line number
        return f"file:///{file_path}:{line_number} - Line {line_number}"

    @staticmethod
    def messageFormatter(msg, loc, type):    

        timestamp = PyLogger.logsData()
        if isinstance(msg, Exception):
            msg = str(msg.args[0]) if msg.args else str(msg)
        shorten = textwrap.shorten(msg, width=1024, placeholder="...") #Cut the message if exceeds 1mb
        logMsg = f"{timestamp} >> {loc} \n{shorten}\n"
        return logMsg

    @staticmethod
    def info(message):
        lineCaller = PyLogger.get_caller_info()
        logs = PyLogger.messageFormatter(message, lineCaller, "INFO")
        print(f"\033[96m{logs}\033[0m")
    
    @staticmethod
    def warning(message):
        lineCaller = PyLogger.get_caller_info()
        logs = PyLogger.messageFormatter(message, lineCaller, "WARNING")
        print(f"\033[93m{logs}\033[0m")
        
    @staticmethod
    def error(message):
        lineCaller = PyLogger.get_caller_info()
        logs = PyLogger.messageFormatter(message, lineCaller, "ERROR" )
        print(f"\033[91m{logs}\033[0m")


