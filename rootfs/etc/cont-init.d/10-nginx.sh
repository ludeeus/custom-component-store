#!/usr/bin/with-contenv bash
###############################################
#  
#  Set NGINX config.
#  
###############################################

if [ -z "${NO_AUTH}" ] || [ "${NO_AUTH}" == false ]; then

  if [ -z "${USERNAME}" ]; then
    echo "Missing username in env USER."
    exit 1
  fi

  if [ -z "${PASSWORD}" ]; then
    echo "Missing password in env PASSWORD."
    exit 1
  fi

  htpasswd -bc /etc/nginx/.htpasswd "${USERNAME}" "${PASSWORD}"

elif [ "${NO_AUTH}" == true ]; then
  echo "NO_AUTH set to true, skipping authentication."

else
  echo "Something went wrong."
  exit 1

fi
