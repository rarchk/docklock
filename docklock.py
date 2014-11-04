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
	def encrypt(self,passpharase,depList,wdir):
		wdir+="/aufs/diff/";
		for i in depList:
			image=i.split('\n')[0]; 
			print wdir+image;
			os.system("tar -cvf "+image".tar "+wdir+image);
			os.system("rm -rf "+wdir+image+"/*");
			os.system("mv "+image+".tar "+wdir+image+"/");
			
			gpg = gnupg.GPG(gnupghome='/root')
			with open(wdir+image+"/"+image+".tar", 'rb') as f:
			    status = gpg.encrypt_file(
			        f, recipients=[''],
			        output= wdir+image+"/"+image+".tar.gpg")

			print 'ok: ', status.ok
			print 'status: ', status.status
			print 'stderr: ', status.stderr

	def decrypt(self,CypherF,SourceF,passphrase):
		 #os.system("echo "+passphrase+"|gpg --passphrase-fd 0  -d "+CypherF+">"+SourceF);
		 os.system("echo "+passphrase+"|gpg --passphrase-fd 0  -d "+CypherF);

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print 'Usage: docklock <Action> <imageid> [passphrase]'
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
	if (sys.argv[1] == 'encrypt'):
		engine.encrypt(sys.argv[3],depList,wdir);
	elif (sys.argv[1] == 'decrypt'):
		engine.decrypt(sys.argv[2],sys.argv[3],depList,wdir);
		
#decrypt()
#gpg = gnupg.GPG(gnupghome='/home/testgpguser/gpghome')
#with open('my-encrypted.txt.gpg', 'rb') as f:
#    status = gpg.decrypt_file(f, passphrase='my passphrase', output='my-decrypted.txt')
#
#print 'ok: ', status.ok
#print 'status: ', status.status
#print 'stderr: ', status.stderr

