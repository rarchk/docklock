
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
A docker container can be seperated into two contexts:
- Image
	- Base Image, taken from popular registery 
	- Properitetry Image, which takes this base registery, and builds a dev environment around it. *(To be encrypted)* 
- Data  
	- Basically volumes, in which your application stores data. *(To be encrypted)*


	  

