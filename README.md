## Requirements
* Python 3.6+

## Install

Install virtualenv and set up a virtual environment

`pip install virtualenv`

`virtualenv venv`

Mac/Linux:
`source venv/bin/activate`

Windows (I think)
`./venv/bin/activate`

Install dependencies

`pip install -r requirements.txt`

## Run

`./start.sh`

## How to use

Ensure MedStore is running on port 4000 and run ngrok pointing at http port 5000.
This will funnel all requests from ngrok through the proxy and to MedStore then displaying the
response from MedStore. This application was designed to be used with black-widow and specifically
with the ShipStation integration hence the proxy response being in XML. The port number was already
modified to point to MedStore but the response content may need to be changed
based on your use case, it should be as simple as changing the response media type from
`application/xml` to `application/json` for JSON content.

