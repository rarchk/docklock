docklock
========

##Securing your containers... Beyond Default
###Features for end-user 
- Security for your system, if your critical applications like browsers, get compromised by providing container isolation.  
- Security for your critical applications like bitcoin wallet, browser histories and other meta data., if your system gets compromised physically. 

### Features for cloud user 
- In general, private registries are secure, and uses ssl/tls channels to make your data private, but due to recent emergence of shellshock or poodle bugs, it will be precautionary if we enable extra layer of encryption on our images. 
 

> Usage 
docklock encrypt <imagename> <passphrase>
docklock decrypt <imagename> <passphrase>
	
