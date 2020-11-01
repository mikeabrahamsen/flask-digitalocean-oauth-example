import os
import requests
from flask import Flask, request, render_template, redirect, url_for
from digital_ocean_client import DigitalOceanClient, ApiError

app = Flask(__name__)

DIGITAL_OCEAN_CLIENT_ID = os.environ.get('DIGITAL_OCEAN_CLIENT_ID')
DIGITAL_OCEAN_CLIENT_SECRET = os.environ.get('DIGITAL_OCEAN_CLIENT_SECRET')


@app.route('/', methods=['GET'])
def index():
    error = request.args.get('error', None)
    client = DigitalOceanClient(DIGITAL_OCEAN_CLIENT_ID,
                                DIGITAL_OCEAN_CLIENT_SECRET)
    return render_template(
        'index.html',
        oauth_url=client.get_authorize_oauth_url(),
        error=error
    )


@app.route('/digitalocean', methods=['GET'])
def link_provider():
    code = request.args.get('code', None)
    error = None
    if code:
        try:
            client = DigitalOceanClient(DIGITAL_OCEAN_CLIENT_ID,
                                        DIGITAL_OCEAN_CLIENT_SECRET)
            token, scope, expiry, refresh_token = client.finish_oauth(code)
            headers = {"Authorization": f"Bearer {token}"}
            api_droplet_list_url = "https://api.digitalocean.com/v2/droplets"

            servers = requests.get(api_droplet_list_url, headers=headers,
                                   timeout=3).json()
            return render_template(
                'server_list.html',
                servers=servers.get('droplets', None)
            )
        except ApiError as e:
            error = f'API Error: {e}'
        except TypeError as e:
            error = f'Error: {e}'
    return redirect(url_for('.index', error=error))
