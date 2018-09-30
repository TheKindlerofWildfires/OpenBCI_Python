import plugin_interface as plugintypes

class PluginNeuralnet(plugintypes.IPluginExtended):
	def activate(self):
		print("Neuralnet activated")
	
	# called with each new sample
	def __call__(self, sample):
		if sample:
            # print impedance if supported
			if self.imp_channels > 0:
				sample_string = "ID: %f\n%s\n%s\n%s" %(sample.id, str(sample.channel_data)[1:-1], str(sample.aux_data)[1:-1], str(sample.imp_data)[1:-1])
			else:
				sample_string = "ID: %f\n%s\n%s" %(sample.id, str(sample.channel_data)[1:-1], str(sample.aux_data)[1:-1])
			print("---------------------------------")
			print(sample_string)
			print("---------------------------------")
		
		# DEBBUGING
		# try:
		#     sample_string.decode('ascii')
		# except UnicodeDecodeError:
		#     print("Not a ascii-encoded unicode string")
		# else:
		#     print(sample_string)
		'''
		So here is the plan!
		Turn on device
		Ask to move arm
		Record about 1 second of time
		fft that data
		store at list sample 1
		rinse and repeat for like 5 samples
		
		continiously store and dump data every 1/2 second
		if it ever looks right go off like an alarm
		Use sklearn to process the data and turn that into 
		'''
		
