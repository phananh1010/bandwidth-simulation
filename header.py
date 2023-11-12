FPS = 29
BUFFER_CAP = 1000 # 1 second

PORT= 11111
IP  = "10.0.0.56"

#input location for FILEPARSER class
INPUT_FILETEMPLATE = './data/compressed_file_size/*'

LOG_FILETEMPLATE = './logs/datapacket_arrival_log_exp{}'
LOG_DELAY        = './logs/delay'

CLIENT   = 'client'
SERVER   = 'server'
DELAY    = 'delay'
DEV_MODE = 'dev_mode'


SIM_MODE_NEW_RUNNING = 'new-run'
SIM_MODE_CONTINUE    = 'continue'


#FILEPARSER ADJUSTMENT PARAMETERS
MSG_SIZE_FACTOR =  2