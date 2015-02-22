import sys
import xml.etree.ElementTree as ET

def main(argv):
	if len(argv) == 3:
		tree = ET.parse(argv[1])
		root = tree.getroot()

		for POINT in root.findall('POINT'):
			f_start, f_end = float(POINT.find('F0_START').text), float(POINT.find('F0_END').text)
			top_hz, bottom_hz = float(POINT.find('TOP_HZ').text), float(POINT.find('BOTTOM_HZ').text)
			
			if f_start > top_hz or f_end < bottom_hz:
				root.remove(POINT)

		tree.write(argv[2])
	else:
		print("Usage: " + argv[0] + " <XML File> <XML File>", file=sys.stderr)
		exit(-1)

if __name__ == '__main__':
	main(sys.argv)