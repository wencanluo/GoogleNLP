'''
File: gSpeechRecognition.py
Author: Wencan Luo
Date: 02/11/2014

Language: 
	'English': ['en-US', 'United States']
	'Chinese':  ['cmn-Hans-CN', 'Mandarin'],
                ['yue-Hant-HK', 'Cantonese']				
'''

import urllib2

class SpeechRecognizer:
	"""
	A simple Speech Recognizier using google speech API. A complete list of support languages can be found at https://www.google.com/intl/en/chrome/demos/speech.html
	"""
	def __init__(self, language = 'en-US'):
		pass
		
	def start(self):
		pass
	
	def getSpeech2Text(self, flac, language = 'en-US'):
		'''
		@param flac: input audio file with flac format, single channel, sample rate = 16000
		@param language: 'en-US' for English; 'cmn-Hans-CN' for Mandarin
		'''
		url = "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang="+language
		audio = open(flac,'rb').read()
		headers={'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
		request = urllib2.Request(url, data=audio, headers=headers)
		response = urllib2.urlopen(request)
		return response.read()

if __name__ == '__main__':
	SR = SpeechRecognizer() 
	language = 'en-US'
	flac = 'howareyou.flac'
	print SR.getSpeech2Text(flac, language)