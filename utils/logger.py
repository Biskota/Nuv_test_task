import logging

logger2 = logging.getLogger(__name__)
logger2.setLevel(logging.INFO)
console_out = logging.StreamHandler()
logger2.addHandler(console_out)
