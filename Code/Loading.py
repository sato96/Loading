import itertools
import threading
import time
import sys
from datetime import datetime



class Loading(object):
	"""docstring Loading
		Class father,it has some useful methods
		this class should not be instantiated
		Init parameters:
		msg: string -> it is the massage during loading
		loadMSG: string -> it is the first message printed
		doneMSG: string -> it is the last massega printed
		lohMsg: Bool -> it is a flag to choos log message in a txt file
	"""
	_timeout: float

	def __init__(self, msg='', loadMSG='Loading', doneMSG='Done!', logMsg=False) -> object:
		self.done = False
		self._msg = msg
		self._loadingMSG = loadMSG
		self._doneMSG = doneMSG
		self._write = ''
		self._logMsg = logMsg
		self._log = []
		#timeout is useful if you want to update your animation faster
		self._timeout = 0.1
		if self._write == '':
			return
		self._log.append({'time': str(datetime.now())[:19], 'msg': self._msg})



	@property
	def done(self):
		return self._done

	@property
	def loadingMSG(self):
		return self._loadingMSG

	@property
	def doneMSG(self):
		return self._doneMSG

	@property
	def msg(self):
		return self._msg

	@property
	def write(self):
		return self._write

	@property
	def logMsg(self):
		return self._logMsg

	@done.setter
	def done(self, value):

		if type(value) == bool:
			self._done = value
			time.sleep(0.1 * 3)

	@loadingMSG.setter
	def loadingMSG(self, value):
		self._loadingMSG = str(value)

	@doneMSG.setter
	def doneMSG(self, value):
		self._doneMSG = str(value)

	@msg.setter
	def msg(self, value):

		self._msg = str(value)
		self._log.append({'time': str(datetime.now())[:19], 'msg': self._msg})

	@write.setter
	def write(self, value):
		self._write = str(value)

	@logMsg.setter
	def logMsg(self, value):
		try:
			self._logMsg = bool(value)
		except:
			print("Bool value invalid")

	def getLogMsg(self):
		return self._log

	def saveLogMsg(self, path=''):

		if self._logMsg:
			if path != '':
				file = path + "/" + "logMsg.txt"
			else:
				file = "logMsg.txt"
			open(file, "w").write(''.join(row['time'] + '  ' + row['msg'] + '\n' for row in self._log))

		else:
			pass

	# here is the animation
	def _Animate(self):
		pass

	# replace
	# do stuff

	def StartAnimation(self):
		t = threading.Thread(target=self._Animate)
		t.start()


class LoadingBar(Loading):
	def __init__(self, msg='', loadMSG='Loading', doneMSG='Done!', logMsg=False):
		super().__init__(msg=msg, loadMSG=loadMSG, doneMSG=doneMSG, logMsg=logMsg)

	def _Animate(self):
		for c in itertools.cycle(['|', '/', '-', '\\']):
			if self.done:
				break
			spaces = self._SetBlancSpaces()
			self._write = '\r' + self.loadingMSG + ' ' + self.msg + ' ' + c + spaces
			sys.stdout.write(self._write)
			# sys.stdout.flush()
			time.sleep(self._timeout)
		spaces = self._SetBlancSpaces()
		sys.stdout.write('\r' + self._doneMSG + spaces + '\n')

	def _SetBlancSpaces(self):
		return len(self._write.rstrip()) * ' '


class LoadingDot(Loading):
	def __init__(self, msg='', loadMSG='Loading', doneMSG='Done!', logMsg=False):
		super().__init__(msg=msg, loadMSG=loadMSG, doneMSG=doneMSG, logMsg=logMsg)
		self._timeout = self._timeout * 3

	def _Animate(self):
		for c in itertools.cycle([' ', '.', '..', '...', '....', '.....', '......']):
			if self.done:
				break
			spaces = self._SetBlancSpaces()
			self._write = '\r' + self.loadingMSG + ' ' + self.msg + ' ' + c + spaces
			sys.stdout.write(self._write)
			# sys.stdout.flush()
			time.sleep(self._timeout)
		spaces = self._SetBlancSpaces()
		sys.stdout.write('\r' + self._doneMSG + spaces + '\n')

	def _SetBlancSpaces(self):
		return len(self._write.rstrip()) * ' '

class LoadingPercentage(Loading):
	def __init__(self, iteration, total, loadingMSG = '', suffix = '', decimals = 1, length=100, fill='█', doneMSG = 'Done!', logMsg = False):
		super().__init__(msg='', loadMSG=loadingMSG, doneMSG=doneMSG, logMsg=logMsg)
		self.decimals = decimals
		self._suffix = suffix
		self._decimals = decimals
		self._length = length
		if fill !=  ' ' * len(fill) and fill != '':
			self._fill = fill.rstrip()
		else:
			self._fill = '█'
		self._iteration = iteration
		self._total = total


	@property
	def suffix(self):
		return self._suffix
	@property
	def fill(self):
		return self._suffix
	@property
	def iteration(self):
		return self._suffix
	@iteration.setter
	def iteration(self, value):
		try:
			self._iteration = int(value)
			self._msg = str(value)
		except:
			pass
	@fill.setter
	def fill(self, value):
		try:
			if value != ' ' * len(value) and value != '':
				self._fill = value.rstrip()
			else:
				self._fill = '█'
		except:
			pass
	@suffix.setter
	def suffix(self, value):
		self._suffix = str(value)



	def _Animate(self):
		print()
		while True:
			percent = ("{0:." + str(self._decimals) + "f}").format(100 * (self._iteration / float(self._total)))
			filledLength = int(self._length * self._iteration // self._total)
			bar = self._fill * filledLength + '-' * (self._length - filledLength) * len(self._fill)
			print(f'\r{self._loadingMSG} |{bar}| {percent}% {self._suffix}', end = '')
			time.sleep(self._timeout)
			if self._iteration >= self._total or self.done == True:
				bar = self._fill * self._length
				percent = '100'
				print(f'\r{self._loadingMSG} |{bar}| {percent}% {self._suffix}', end='\n')
				break
		self.done = True
		print()

