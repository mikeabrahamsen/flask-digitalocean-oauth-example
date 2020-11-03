# flask-digitalocean-oauth-example
Supplement project code showing an example of OAuth with Digital Ocean

# Add Necessary Environment Variables 

The easiest way to do this is to create a `.flaskenv` file with the following
information provided:

```sh
FLASK_ENV=development
DIGITAL_OCEAN_CLIENT_ID = "found at https://cloud.digitalocean.com/account/api/applications"
DIGITAL_OCEAN_CLIENT_SECRET = "found at https://cloud.digitalocean.com/account/api/applications"
```

# Run the application

`flask run`
