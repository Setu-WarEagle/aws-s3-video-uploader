## aws-s3-video-uploader
###### This repo contains a python experiment code to upload files/videos to S3 buckets using flask,boto3. This test app gets packaged in a Docker image and runs in an EC2 instnance.

Tutorial followed : https://stackabuse.com/file-management-with-aws-s3-python-and-flask/

---

##### Preserving bootstrap steps needed to prepare the EC2 instance
```
# get dependencies
yum install wget -y
yum groupinstall "Development Tools" -y
yum install zlib-devel -y
yum install libffi-devel -y
yum install openssl-devel -y

#install python
#check for the latest release: https://www.python.org/downloads/ and replace the version accordingly.
wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tar.xz
tar xf Python-3.*
cd Python-3.7.6
./configure
make
make install
echo "export PATH=$PATH:/usr/local/bin" > /etc/profile.d/videouploader.sh  # creating a custom profile in /etc/profile.d for python3

# install awscli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# install docker
sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install docker-ce-3:18.09.1-3.el7 -y
```
