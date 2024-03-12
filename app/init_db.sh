#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    source .env
fi

# Array of user data
users=(
    '{"parameter": {"id": 0, "name": "Cesar", "lastname": "Marquez", "email": "ces.mar@gmail.com"}}'
    '{"parameter": {"id": 0, "name": "Arnaldo", "lastname": "Lito", "email": "arn.lit@gmail.com"}}'
    '{"parameter": {"id": 0, "name": "Juan Jose", "lastname": "Blaz", "email": "jj.bla@gmail.com"}}'
    '{"parameter": {"id": 0, "name": "Ricardo", "lastname": "Montes", "email": "ric.mon@gmail.com"}}'
    '{"parameter": {"id": 0, "name": "Facundo", "lastname": "Agustino", "email": "fac.ag@gmail.com"}}'
    '{"parameter": {"id": 0, "name": "Almendra", "lastname": "Rivera", "email": "alm.riv@gmail.com"}}'
    '{"parameter": {"id": 0, "name": "Victoria", "lastname": "Caceres", "email": "vic.cac@gmail.com"}}'
    '{"parameter": {"id": 0, "name": "Lucas", "lastname": "Mendez", "email": "luc.men@gmail.com"}}'
)

# Use the HOST variable
echo "HOST API: $API_HOST"

# Iterate over user data and make curl requests
for user_data in "${users[@]}"; do
    curl --location "$API_HOST/api/v1/create_user" \
        --header 'Content-Type: application/json' \
        --data-raw "$user_data"
done
