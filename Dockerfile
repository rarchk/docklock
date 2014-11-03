# This file lets user create a base repository, which act as public repository.
# Author: Ronak Kogta
# Date: Nov 3, 2014


FROM ubuntu:14.04
MAINTAINER Ronak Kogta "tau.ronak@gmail.com"

# basic docker file
# For this example, we want ssh in our every base image then we install this dependency here.

RUN apt-get update -y && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]   

# You can provide further basic things in this dockerfile. 
# . 
# . 
# .
# . 
