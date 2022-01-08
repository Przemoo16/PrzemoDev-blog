import pprint
from typing import Any
from urllib import parse

import requests

BASE_URL = "https://login.salesforce.com"
AUTH_ENDPOINT = "/services/oauth2/authorize"
TOKEN_ENDPOINT = "/services/oauth2/token"  # nosec
USER_INFO_ENDPOINT = "/services/oauth2/userinfo"

CLIENT_ID = "YOUR_CONSUMER_KEY"
CLIENT_SECRET = "YOUR_CONSUMER_SECRET"  # nosec
REDIRECT_URI = "http://localhost:8080/oauth2/callback"
SCOPES = ["api", "refresh_token"]


def create_authorization_url(
    client_id: str, redirect_uri: str, scopes: list[str]
) -> str:
    quoted_client_id = parse.quote(client_id)
    quoted_redirect_uri = parse.quote(redirect_uri)
    quoted_scopes = parse.quote(" ".join(scopes))
    return (
        f"{BASE_URL}{AUTH_ENDPOINT}"
        "?response_type=code"
        f"&client_id={quoted_client_id}"
        f"&redirect_uri={quoted_redirect_uri}"
        f"&scope={quoted_scopes}"
    )


def get_access_info(
    auth_code: str,
    client_id: str,
    client_secret: str,
    redirect_uri: str,
) -> dict[str, Any]:
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
    }
    res = requests.post(f"{BASE_URL}{TOKEN_ENDPOINT}", data=data)
    res.raise_for_status()
    return res.json()


def get_user_info(access_token: str, instance_url: str) -> dict[str, Any]:
    headers = {"Authorization": f"Bearer {access_token}"}
    res = requests.get(f"{instance_url}{USER_INFO_ENDPOINT}", headers=headers)
    res.raise_for_status()
    return res.json()


def refresh_access_token(
    client_id: str, client_secret: str, refresh_token: str
) -> dict[str, Any]:
    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
    }
    res = requests.post(f"{BASE_URL}{TOKEN_ENDPOINT}", data=data)
    res.raise_for_status()
    return res.json()


def main() -> None:
    pp = pprint.PrettyPrinter(indent=4)

    auth_url = create_authorization_url(CLIENT_ID, REDIRECT_URI, SCOPES)
    print("Authorization URL:", auth_url)

    auth_code = parse.unquote(input("Code:"))

    access_info = get_access_info(auth_code, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    print("Access info:")
    pp.pprint(access_info)

    access_token = access_info["access_token"]
    instance_url = access_info["instance_url"]
    user_info = get_user_info(access_token, instance_url)
    print("User info:")
    pp.pprint(user_info)

    refresh_token = access_info["refresh_token"]
    refreshed_token_info = refresh_access_token(CLIENT_ID, CLIENT_SECRET, refresh_token)
    print("Refreshed token info:")
    pp.pprint(refreshed_token_info)


if __name__ == "__main__":
    main()
