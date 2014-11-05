#------------------------------------------------#
#------------------- Dock Lock-------------------#
# 	Security beyond Default			 #
# 
#Authors : Ronak Kogta#
#Following package uses gpg symmetric encryption alogrithm to encrypt your container images

#!/usr/bin/env python
import os,sys; 
import gnupg,tarfile

class docklock:
	keydir=""
	email=""
	def init(self):
		self.keydir=raw_input("Enter Directory where your keys are stored: ")
		flag=raw_input("Want to generate key: y/n ");
		if flag == 'y' or flag == 'Y' or flag == 'yes':
			cDr=os.getcwd();
			os.chdir(self.keydir);
			os.system("gpg --gen-key");
			os.chdir(cDr);
		else: 
			print "You are good to go!!"
			print 		
	def encrypt(self,depList,wdir):
		self.email=raw_input("Set Signature for your mail<email id>: ")
		wdir+="/aufs/diff/";
		cDr=os.getcwd()
		for i in depList:
			image=i.split('\n')[0];
			print wdir+image; 
			os.system("tar -cf "+image+".tar "+wdir+image);
			os.system("rm -rf "+wdir+image+"/*");
						
			gpg = gnupg.GPG(gnupghome=self.keydir)
			with open(image+".tar", 'rb') as f:
			    status = gpg.encrypt_file(
			        f, recipients=[self.email],
			        output= image+".tar.gpg")
		#	print 'ok: ', status.ok
		#	print 'status: ', status.status
		#	print 'stderr: ', status.stderr
			os.system("mv "+image+".tar.gpg "+wdir+image+"/");
			os.system("rm "+image+".tar");

	def decrypt(self,depList,wdir):
		 secret=raw_input("Enter your passphrase: ")
		 wdir+="/aufs/diff/";
		 cDr=os.getcwd();
		 for i in depList:
			image=i.split('\n')[0]; 
			print wdir+image;
			
						
			gpg = gnupg.GPG(gnupghome=self.keydir)
			with open(wdir+image+"/"+image+".tar.gpg", 'rb') as f:
			    status = gpg.decrypt_file(f, passphrase=secret,
			    	output= image+".tar")
		#	print 'ok: ', status.ok
		#	print 'status: ', status.status
		#	print 'stderr: ', status.stderr
			
		    	os.system("tar xf "+image+".tar");
		    	try:
		    		os.system("mv "+str(wdir[1:])+image+"/* "+wdir+image+"/")
		    	except:
		    		continue;	
		    	os.system("rm -rf "+str(wdir[1:])+image)

		   	os.system("rm "+image+".tar")
		    	os.system("rm "+wdir+image+"/"+image+".tar.gpg")
			


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Usage: docklock <Action> <imageid>'
		sys.exit(1);
	
	aufsList='';
	depList=[]
	wdir="/var/lib/docker"

	# getting layers corresponding to this image 
	for root, dirs, files in os.walk(wdir+"/aufs/layers"):
		aufsList=files
		
	for i in aufsList: 
		if(sys.argv[2] in i):
			fp=open(wdir+"/aufs/layers/"+i,'r');
			buff=fp.readlines();
			fp.close();
			depList.append(i);
			depList+=buff;
			break;
	if len(depList) ==0:
		print "Error: no such imageid"
		sys.exit(-1);

	engine=docklock();
	engine.init();
	if (sys.argv[1] == 'encrypt'):
		engine.encrypt(depList,wdir);
	elif (sys.argv[1] == 'decrypt'):
		engine.decrypt(depList,wdir);
		
