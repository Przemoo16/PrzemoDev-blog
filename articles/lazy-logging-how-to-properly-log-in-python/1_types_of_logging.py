# pylint: disable=logging-not-lazy
# pylint: disable=logging-format-interpolation
# pylint: disable=logging-fstring-interpolation
# pylint: disable=consider-using-f-string

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log_arg = "Hello"

# Eager logging
log.info("Sample message: %s" % log_arg)  # %-formatting
log.info("Sample message: {}".format(log_arg))  # str.format()
log.info(f"Sample message: {log_arg}")  # f-strings

# Eager logging with explicit steps
message_1 = "Sample message: %s" % log_arg
log.info(message_1)
message_2 = "Sample message: {}".format(log_arg)
log.info(message_2)
message_3 = f"Sample message: {log_arg}"
log.info(message_3)

# Lazy logging
log.info("Sample message: %s", log_arg)
