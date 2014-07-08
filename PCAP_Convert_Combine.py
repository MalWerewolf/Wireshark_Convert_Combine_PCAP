import sys, os, argparse, time

"""
The Following Conditions must be met for this script to work:
	(These Conditions could easily be modified)
	* Folder Paths are set to windows
	* Editcap.exe & Mergecap.exe are located in "C:\Program Files\Wireshark"
"""

def_dir = os.getcwd()

parser = argparse.ArgumentParser(
	description = '''This program will convert all encapsulated files and combine them into a single PCAP from a specified folder path. This is done by using wireshark's editcap & mergecap.''',
	epilog = '''Example Usage: PCAP_Convert_Combine.py -f "C:\Folder Contains PCAPS\" -o "C:\Folder Contains PCAPS\MERGED\MERGED.pcap" -ien erf -iex gz -oen ether -oex libpcap''')
parser.add_argument('-f', type=str, default=def_dir+"\\", help='Folder path containing PCAPs.')
parser.add_argument('-o', type=str, default=def_dir+"\MERGED.pcap", help='Output Folder+Filename of MERGED PCAP.')
parser.add_argument('-ien', type=str, default="erf", help='Encapsulation Type of INPUT files. (Errors will show you options)')
parser.add_argument('-iex', type=str, default="gz", help='Extension of INPUT files.')
parser.add_argument('-oen', type=str, default="ether", help='Encapsulation Type of OUTPUT files. (Errors will show you options)')
parser.add_argument('-oex', type=str, default="libpcap", help='Extension of OUTPUT files.')
args = parser.parse_args()
count = 0

for file in os.listdir(args.f):
	if file.endswith(args.iex):
		count += 0.25
		EDIT_CMD = "\"c:\\Program Files\\Wireshark\\editcap.exe\" -F " + args.oex + " -T " + args.ien + " " + args.f + file + " " + args.f + "EDIT-" + file
		os.system(EDIT_CMD)

print "Pausing for", count, "seconds for files to be created."
time.sleep(count)
MERGE_CMD = "\"c:\\Program Files\\Wireshark\\mergecap.exe\" -F " + args.oex + " -T " + args.oen + " -w " + args.o + " "

for file in os.listdir(args.f):
	if file.startswith("EDIT-") and file.endswith(args.iex):
		MERGE_CMD = MERGE_CMD + args.f + file + " "

os.system(MERGE_CMD)

for file in os.listdir(args.f): #Cleanup
	if file.startswith("EDIT-") and file.endswith(args.iex):
		os.remove(file)

print "Completed! Merged (and converted) PCAP should be at " + args.o