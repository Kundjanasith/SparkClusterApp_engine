FROM    centos:latest

# Enable Extra Packages for Enterprise Linux (EPEL) for CentOS
RUN  yum install -y epel-release
# Install Node.js and npm
RUN yum install -y nodejs npm
RUN yum install -y git
RUN npm install -g forever


# Install app dependencies
COPY package.json /src/package.json
RUN cd /src; npm install --production

# Bundle app source
COPY . /src

EXPOSE  10050

#CMD ["forever", "start", "/src/server.js"]
CMD ["node", "src/server.js"]
