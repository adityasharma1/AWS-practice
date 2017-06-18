import logging
logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('log_files\logging_module.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)