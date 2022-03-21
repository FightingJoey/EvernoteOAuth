import os
import sys

from evernote.api.client import EvernoteClient

from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect


def get_evernote_client(token=None):
    if token:
        return EvernoteClient(token=token, sandbox=True)
    else:
        return EvernoteClient(
            consumer_key='EN_CONSUMER_KEY',
            consumer_secret='EN_CONSUMER_KEY',
            sandbox=True
        )


def index(request):
    return render(request, 'oauth/index.html')


def auth(request):
    client = get_evernote_client()
    callbackUrl = 'http://%s%s' % (
        request.get_host(), reverse('evernote_callback'))
    request_token = client.get_request_token(callbackUrl)

    # Save the request token information for later
    request.session['oauth_token'] = request_token['oauth_token']
    request.session['oauth_token_secret'] = request_token['oauth_token_secret']

    # Redirect the user to the Evernote authorization URL
    return redirect(client.get_authorize_url(request_token))


def callback(request):
    try:
        client = get_evernote_client()
        client.get_access_token(
            request.session['oauth_token'],
            request.session['oauth_token_secret'],
            request.GET.get('oauth_verifier', '')
        )
    except KeyError:
        return redirect('/')

    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()

    return render(request, 'oauth/callback.html', {'notebooks': notebooks})


def reset(request):
    return redirect('/')
