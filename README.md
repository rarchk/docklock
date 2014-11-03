docklock
========
##Securing your containers... Beyond Default
###Features for end-user 
- Security for your system, if your critical applications like browsers, get compromised by providing container isolation.  
- Security for your critical applications like bitcoin wallet, browser histories and other meta data., if your system gets compromised physically. 

### Features for cloud user 
- In general, private registries are secure, and uses ssl/tls channels to make your data private, but due to recent emergence of shellshock or poodle bugs, it will be precautionary if we enable extra layer of encryption on our images. 
- So we provide a zero knowledge feature for registery services like quay.io etc.
 

####Usage 
```bash 
docklock encrypt <imagename> <passphrase>
docklock decrypt <imagename> <passphrase>
```	
###Workflow
A docker container can be seperated into two contexts:
- Image
	- Base Image, taken from popular registery 
	- Properitetry Image, which takes this base registery, and builds a dev environment around it. *(To be encrypted)* 
- Data  
	- Basically volumes, in which your application stores data. *(To be encrypted)*


 [Easy task, as we know where volumes are... ]


[Tricky task, as these images will keep changing, plus also base images can change too] (keeping it static is the toughest job, though docker has simplifed the problem greatly)
	  

