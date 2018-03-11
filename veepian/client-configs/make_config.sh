#!/bin/bash

# First argument: Client identifier

OVPN_DIR=/etc/openvpn
KEY_DIR=~/openvpn-ca/keys
#CLIENT_DIR="${KEY_DIR}/${1}"
OUTPUT_DIR=~/client-configs/files
BASE_CONFIG=~/client-configs/base.conf
#mkdir ${CLIENT_DIR}

echo "Generating client keys..."

#sudo -s << EOF

#cd ${OVPN_DIR}/easy-rsa
#SERVERNAME=${2}
#HOSTNAME=${1}
#source ./vars
#./pkitool ${1}
#cp keys/${1}.crt keys/${1}.key ${CLIENT_DIR}

#EOF

echo "Making client configuration file..."

cat ${BASE_CONFIG} \
    <(echo -e '<ca>') \
    ${KEY_DIR}/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    ${KEY_DIR}/${1}.crt \
    <(echo -e '</cert>\n<key>') \
    ${KEY_DIR}/${1}.key \
    <(echo -e '</key>\n<tls-auth>') \
    ${KEY_DIR}/ta.key \
    <(echo -e '</tls-auth>') \
    > ${OUTPUT_DIR}/${1}.ovpn

#sed -i "s/DEST_IP/${2}/g" ${OUTPUT_DIR}/${1}.ovpn

# echo "Removing client key directory..."

# rm -rf ${CLIENT_DIR}

echo "Completed!"
