import json
import re
import os
import subprocess
from core.tools.Astor import Astor
from pprint import pprint

class AdqFix(Astor):
	"""docstring for AdequateFix"""
	def __init__(self):
		super(AdqFix, self).__init__(name="AdqFix")

	def run(self, 
		project, 
		id):
		self.runAstor(project, id, mode="adqfix")