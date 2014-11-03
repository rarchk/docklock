Dockerfiles 
=== 
- image reprsentation 

+ from <image>
+ run apt-get install -y memcached (executes any command on the current image and commit the results )
+ MAINTAINER <name> <email>
+ ENTRYPOINT <command> (triggers command as soon as container is launched)
+ ENTRYPOINT ["ls","-l"];
+ USER daemon (when running the iamge)
+ ADD <src> <dest> # copy a file 
+ ENV <key> <Value>
+ CMD["executable","param#1","param#2"] # just like exec
+ CMD ["param#1","param#2"] # default parameters to entrypoint 
+EXPOSE 80
+ VOLUME /data #create data volume

Ship it! (units of software delivery)
- run everywhere 
	- regardless of kernel version and host distro but container and host arch must match(unless you emulate CPU with qemu and binfmt)
- run anything 


Seperation of concerns 
- code,library,package manager, app, data all mine
- logging,remote access, network configuration, monitoring 

pid,mnt,net,uts,ipc,user
memory,cpu,blkio,devices,though no device emulation

Capabilities 
- cap_ipc_lock,cap_lease,cap_mknod,cap_net_admin,cap_net_bind_service,capt_net_raw,cap_sys_admin
- grsec,seccomp,setns,seccomp-bpf

Copy on write storage 
unioning FS - AUFS overlayfs 
snapshotting filesysstems  - BTRFS,zFS  (thin snapshots with lvm or device mapper)

Compute efficiency 
- native cpu perf 
- a little memory overhead 
- a little network overhead, can be reduced to zero 


Links
- a way to connect one container to other 
- will cpose the child container's exposed ports, ip and environment to parent 
- environment vars are prefixed with the alias of child,  

docker -d (detached mode)
	   -p (expose ports)	
