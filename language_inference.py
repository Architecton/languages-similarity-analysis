import numpy as np
import os
from pathlib import Path
from lib_naloga2 import language_inferer

########################
# Author: Jernej Vivod #
########################

# This script provides the human to computer interface for language inference functionality.

# Load reference documents dictionary and dictionary for decoding OHCHR language codes.
references_dicts = np.load('triplets_dicts.npy').item()

if __name__ == "__main__":
	# Prompt user for document name. Keep prompting until entered document name is valid.
	while True:
		print('Documents in \'./data/language_analysis_data\':')
		print("##################")
		for f in os.listdir(os.getcwd() + '/data/language_analysis_data'):
			print(f)
		print("##################\n")

		document_name = input('Enter name of document to analyze (make sure the document is located in ./data/language_analysis_data): ')
		document_full_path = Path("./data/language_analysis_data/" + document_name)

		# Check if document exists.
		if document_full_path.is_file():
			# Create new instance of LanguageAnalyzer class and run analysis.
			la = language_inferer.LanguageAnalyzer(references_dicts)
			la.run(3, document_name)
			break;
		else:
			print('\ndocument \'{0}\' not found. Make sure the document is located in ./data/language_analysis_data folder.\n'.format(document_name))
else:
	def infer_language(document_full_path):
		document_full_path = Path(document_full_path)
		# Create new instance of LanguageAnalyzer class and run analysis.
		la = language_inferer.LanguageAnalyzer(references_dicts)
		la.run(3, document_name)