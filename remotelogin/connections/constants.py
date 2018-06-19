__author__ = 'Filinto Duran (duranto@gmail.com)'
# CAPABILITIES
CAN_BE_MANAGED = 1
CAN_TRANSFER_FILES = 1 << 1
CAN_EXECUTE_COMMANDS = 1 << 2
CAN_HAVE_MULTIPLE_CLIENTS = 1 << 3
CAN_HAVE_MULTIPLE_USER = 1 << 4
CAN_HAVE_MULTIPLE_SESSIONS_PER_USER = 1 << 5
CAN_HAVE_INTERACTIVE_COMMANDS = 1 << 6
CAN_OPEN_MULTIPLE_CHANNELS = 1 << 7
CAN_DO_ALL = (1 << 20) - 1

OPEN = 'NO_RETRIES_ON_OPEN'
DO_NOT_RETRY_ON_OPEN = OPEN

SOCKET_RECV_NOT_READY = None

UNIQUE_PROMPT_FORMAT = '@@{random}PROMPT@@'
UNIQUE_PROMPT_RE = r'\\@\\@\S+PROMPT\\@\\@'


