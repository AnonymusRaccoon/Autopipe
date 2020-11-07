from abc import ABC, abstractmethod
from typing import Generator
import logging


class APData:
	def __init__(self):
		self.value = None
		self.type = None


class Pipe(ABC):
	def __init__(self):
		logging.info(f"Entering pipe: {self.name}")

	@property
	@abstractmethod
	def name(self):
		raise NotImplementedError

	def pipe(self, data: APData) -> APData:
		pass


class Input(ABC):
	def __init__(self):
		logging.info(f"Starting input manager: {self.name}")

	@property
	@abstractmethod
	def name(self):
		raise NotImplementedError

	@abstractmethod
	def generate(self) -> Generator[APData]:
		raise NotImplementedError

	@abstractmethod
	@property
	def loop_cooldown(self) -> int:
		"""
		If negative or 0, the input can't be chained and once the generator return the program will exit.
		If grater then 0, the generator will be called again after a sleep of x seconds where x is the return of this.
		"""
		raise NotImplementedError