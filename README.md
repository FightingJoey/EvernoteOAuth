Django with OAuth
------------------------------------
Web applications must use OAuth to authenticate to the Evernote service. 

1. Open the file `oauth/views.py`
2. Fill in your Evernote API consumer key and secret.
3. On the command line, run the following command to start the sample app:

    ```bash
    $ python manage.py runserver
    ```

4. Open the sample app in your browser: `http://127.0.0.1:8000/`

## OAuth ##
```python
client = EvernoteClient(
    consumer_key='YOUR CONSUMER KEY',
    consumer_secret='YOUR CONSUMER SECRET',
    sandbox=True # Default: True
)
request_token = client.get_request_token('YOUR CALLBACK URL')
print(request_token)
# {'oauth_token': 'geselle-joy.17F9C2F7DB2.687474703A2F2F3132372E302E302E313A383030302F.CE5277C172B4DCB98415DEC7CD9FA5C2', 'oauth_token_secret': '4AFF0DD081CC1555653907C9907F0BE4', 'oauth_callback_confirmed': 'true'}
url = client.get_authorize_url(request_token)
print(url)
# http://127.0.0.1:8000/?oauth_token=geselle-joy.17F9C2F7DB2.687474703A2F2F3132372E302E302E313A383030302F.CE5277C172B4DCB98415DEC7CD9FA5C2&oauth_verifier=EABF08D4B266982C0191FCDB65F0B1EE&sandbox_lnb=false
```
To obtain the access token
```python
access_token = client.get_access_token(
    request_token['oauth_token'],
    request_token['oauth_token_secret'],
    request.GET.get('oauth_verifier', '')
)
```
Now you can make other API calls
```python
client = EvernoteClient(token=access_token)
note_store = client.get_note_store()
notebooks = note_store.listNotebooks()
```

