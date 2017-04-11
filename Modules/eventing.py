from threading import Timer
import server
from queue import PriorityQueue
import datetime

jobs = PriorityQueue()

def send(delay, what):
	when = datetime.datetime.now()
	jobs.put((when + delay, what))