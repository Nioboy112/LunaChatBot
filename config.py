HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "6618564239:AAFocGP8FrjZCRQ3U4ur0vaV5IORfpQq-cA"
    ARQ_API_KEY = "NZICGZ-VLTUNJ-VRNHZG-RWPPBR-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
