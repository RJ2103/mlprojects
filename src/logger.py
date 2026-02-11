# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )


# import logging
# import os
# from datetime import datetime

# LOG_DIR = "logs"
# os.makedirs(LOG_DIR, exist_ok=True)

# LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# logger = logging.getLogger()




# import logging
# import os
# from datetime import datetime

# LOG_DIR = "logs"
# os.makedirs(LOG_DIR, exist_ok=True)


# LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# logger = logging.getLogger()


import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    datetime.now().strftime("%m_%d_%Y_%H_%M_%S.log")
)

logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("mlproject")
