import json
import sys
import collections


def test(words):
	for elem in words.blood_word:
		if elem in words.die_word:
			return True
	return False


def main(argv):
	if len(argv) == 2:
		with open(argv[1]) as json_data:
			data = json.load(json_data)
			result_list = []
			LanguageWords = collections.namedtuple("LanguageWords", "language,classifications,blood_word,die_word")

			for datalist in data:
				blood_word = datalist[2].split(", ")
				die_word = datalist[3].strip().split(", ")		
				language = datalist[0]
				words = LanguageWords(language=language,classifications=datalist[1],blood_word=blood_word, die_word=die_word)
				result_list.append(words)			
			result = [elem for elem in result_list if test(elem)]
			print(result)
	else:
		print("Usage: " + argv[0] + " <JSON File>", file=sys.stderr)
		exit(-1)	

if __name__ == '__main__':
	main(sys.argv)