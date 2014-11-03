#------------------------------------------------#
#------------------- Dock Lock-------------------#
# 	Security beyond Default			 #
# 
#Authors : Ronak Kogta, Shashank Sahni, Gaurav Rajput#
# Following package uses gpg symmetric encryption alogrithm to encrypt your container images

#!/usr/bin/env python
import os,sys; 

class docklock:
	def encrypt(self,SourceF,passpharase):
		 os.system("echo "+passpharase+"|gpg --passphrase-fd 0  -c "+SourceF);
	
	def decrypt(self,CypherF,SourceF,passphrase):
		 #os.system("echo "+passphrase+"|gpg --passphrase-fd 0  -d "+CypherF+">"+SourceF);
		 os.system("echo "+passphrase+"|gpg --passphrase-fd 0  -d "+CypherF);

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print 'Usage: docklock [SourceF] [action] [passphrase]'
		sys.exit(1);
	
	engine=docklock();
	if (sys.argv[2] == 'encrypt'):
		engine.encrypt(sys.argv[1],sys.argv[3]);
	elif (sys.argv[2] == 'decrypt'):
		engine.decrypt(sys.argv[1],str(sys.argv[1].split('.')[:-1]),sys.argv[3]);
		
