import sys, string, pycdlib

def banner():
	print("##########################################");
	print("# VTSTech-ISOScan v0.0.1                 #");
	print("# Facebook: fb.me/VTSTech                #");
	print("# Twitter: @VTSTech_                     #");
	print("# Web: www.VTS-Tech.org                  #");
	print("# E-mail: veritas@vts-tech.org           #");
	print("# BTC 1ByfBujg9bnmk1XXY2rxY6obhqHMUNiDuP #");
	print("##########################################\n");
           	
if len(sys.argv) == 1:
	banner()
	print('Usage: VTSTech-ISOScan.py -t FIND_THIS -p AT_POSITION -s SEARCH_SIZE "C:\ISO\Backup File.iso"\n\nOptions:\n\n-t Find this target string\n-p Check at this position, default searches entire search size\n-s Search this many bytes of each file (Default: 24)');
	sys.exit()
print("##########################")
print("# VTSTech-ISOScan v0.0.1 #")
print("##########################\n\n")
iso = pycdlib.PyCdlib()
needle=str("")
pos=int(0)
search=int(24)
x=int(0)
if (sys.argv[1] == "-t"):
	needle=str(sys.argv[2])
if (sys.argv[3] == "-p"):
	pos=int(sys.argv[4])
if (len(sys.argv) >= 5):
	if (sys.argv[5] == "-s"):
		pos=int(sys.argv[6])
		iso.open(sys.argv[7])
	if (str.lower(sys.argv[5][-4:]) == str(".iso")):
		#print("DEBUG: argv 5 opened!\n")
		iso.open(sys.argv[5])		

print("Target Header: "+str(needle)+"\n")

if (needle == str("")):
	print("Error in syntax! -t must be specified.")
	sys.exit()
if (str.lower(sys.argv[3][-4:]) == str(".iso")):	
	#print("DEBUG: argv 3 opened!\n")
	iso.open(sys.argv[3])
		
for dirname, dirlist, filelist in iso.walk(iso_path='/'):
	for target in filelist:
		if (len(dirname) == 0):
			fn = target
		else:
			fn = dirname+"/"+target
		with iso.open_file_from_iso(iso_path=str(fn)) as infp:
			first = infp.read(int(search))
			if (pos != int(0)):
				if (first[int(pos):(len(needle)+int(pos))] == str.encode(needle)):
					print("Target Detected!:"+fn.replace("//","/"))
			else:
				for x in range(0,int(search)):
					#print("DEBUG:"+str(len(needle)-int(x)))
					if (first[int(x):(len(needle)-int(x))] == str.encode(needle)):
						print("Target Detected!:"+fn.replace("//","/"))
iso.close()