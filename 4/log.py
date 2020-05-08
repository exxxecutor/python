from datetime import datetime

LOGFILE = 'log.txt'

CRE = 'CRE'
INF = 'INF'
ERR = 'ERR'


def log(key, msg):
	with open(LOGFILE, 'a') as logf:
		logf.write(f'{key} --- {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} --- {msg}\n')
