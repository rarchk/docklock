
##Securing your containers... Beyond Default

**Docklock** lets you encrypt your images and critical data, and allows a zero knowledge registery in third party registery services like quay.io. or docker public registery.  

###Inspiration
With recent emergence of heartbleed & poodle bug, we need to consider take extra measures to protect our assets. We liked the spideroak's zero knowledge idea to tackle on the very issue. 

###Use case for end-user  
- Protect your system, if critical applications like browsers get compromised, by providing container isolation.  
- Protect your critical applications like bitcoin wallet, browser data and other meta data, if your system gets compromised physically. 
- Takes a little compute/memory overhead.  


####Usage 
```bash 
docklock encrypt <imagename> <passphrase>
docklock decrypt <imagename> <passphrase>
```	
###Workflow
``` bash 
Base image 
		-- Dockerfiles -- custom images -- containers
						  					-- data only containers (volumes) 
							 				-- normal epipheral containers (only for compute) 
```							
A docker container can be seperated into three contexts:

- Dockerfiles 
	- if application is small, all of images can be represented in this form. So just have to create 
	  password protected archive
- Image
	- Base Image, taken from popular registery 
	- Properitetry Image, which takes this base registery, and builds a dev environment around it. *(To be encrypted)* 
- Persistent Data   
	- Basically volumes, in which your application stores data. *(To be encrypted)*
	- should be stored somewhere safe, like S3/Dropbox/AnyOtherStorageService with zero knowledge principle.
	- Or can stay in server... during runtime, which can be protected by firewalling the VM. 


