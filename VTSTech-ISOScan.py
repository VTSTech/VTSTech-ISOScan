import sys, string, pycdlib

def banner():
	print("##########################################");
	print("# VTSTech-ISOScan v0.0.2                 #");
	print("# Facebook: fb.me/VTSTech                #");
	print("# Twitter: @VTSTech_                     #");
	print("# Web: www.VTS-Tech.org                  #");
	print("# E-mail: veritas@vts-tech.org           #");
	print("# BTC 1ByfBujg9bnmk1XXY2rxY6obhqHMUNiDuP #");
	print("##########################################\n");
           	
if len(sys.argv) == 1:
	banner()
	print('Usage: VTSTech-ISOScan.py -t FIND_THIS -p AT_POSITION -s SEARCH_SIZE -f EXT "C:\ISO\Backup File.iso"\n\nOptions:\n\n-t Find this target string\n-p Check at this position, default searches entire search size\n-s Search this many bytes of each file (Default: 24)\n-f Do not show EXT files');
	sys.exit()

print("##########################")
print("# VTSTech-ISOScan v0.0.2 #")
print("##########################\n\n")

iso = pycdlib.PyCdlib()
needle=str("")
pos=int(0)
search=int(24)
x=int(0)
ext=str("")

for x in range(0,len(sys.argv)):
	if (sys.argv[x] == "-t"):
		needle=str(sys.argv[x+1])
	if (sys.argv[x] == "-p"):
		pos=int(sys.argv[x+1])
	if (sys.argv[x] == "-s"):
		search=int(sys.argv[x+1])
	if (sys.argv[x] == "-f"):
		ext=str(sys.argv[x+1])
	if (str.lower(sys.argv[x][-4:]) == str(".iso")):
		iso.open(sys.argv[x])

#print("DEBUG:"+needle+" "+str(pos)+" "+str(search)+" "+ext)

if (needle == str("")):
	print("Error in syntax! -t must be specified.")
	sys.exit()
	
if (len(ext) >=1):
	print("Target Header: "+str(needle)+" Filtered File Extention: "+str.upper(ext)+"\n")
else:
	print("Target Header: "+str(needle)+"\n")

for dirname, dirlist, filelist in iso.walk(iso_path='/'):
	for target in filelist:
		if (len(dirname) == 0):
			fn = target
		else:
			fn = dirname+"/"+target
		with iso.open_file_from_iso(iso_path=str(fn)) as infp:
			first = infp.read(int(search))
			if (pos != int(0)):
				haystack=first[int(pos):(len(needle)+int(pos))]
				if (haystack == str.encode(needle)):
					print("Target Detected!:"+fn.replace("//","/"))
			else:
				x=int(0)
				for x in range(0,int(search)):
					haystack=first[int(x):(len(needle)+int(x))]
					if (str.lower((fn[-5:-2])) != str.lower(ext)):
						if (haystack == str.encode(needle)):
							print("Target Detected!:"+fn.replace("//","/"))
iso.close()