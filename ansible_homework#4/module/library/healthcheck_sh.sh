#!/bin/bash
# WANT_JSON

addr=$(cat $1 | grep -Po '(?<="addr": ")(.*?)(?=")')
tls=$(cat $1 | grep -Po '(?<="tls": )(.*?)(?=,)')

status_code=`curl -sIL $addr | grep ^HTTP/ |tail -n1 | cut -d ' ' -f 2`

if [[ "${status_code}" == '200' ]]; then
    echo "{\"status_code\": \"$status_code\", \"msg\": \"Web server is OK\"}"

elif [[ "${status_code}" -ne 200 ]]; then
    echo "{\"status_code\": \"$status_code\", \"msg\": \"Web server $addr is not OK, please, check it!\", \"failed\": \"true\" }"
fi