# python-holidays-generator

This sample will show you to easily create a Markdown file for your Holidays Calendar using Nylas Python SDK.

You can follow along step-by-step in our Livestream ["Holidays Calendar with Nylas APIs"]([https://www.nylas.com/blog/how-to-send-emails-with-the-nylas-python-sdk/](https://twitter.com/i/broadcasts/1OwxWzLpVnZJQ)).

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
V3_API_KEY = ""
CALENDAR_ID = ""
GRANT_ID = ""
HOLIDAY_CALENDAR = ""
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip3 install nylas
```

## Usage

Run the script using the `python3` command:

```bash
$ python3 Holidays_Generator.py year_we_want
```

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/python-sdk/) to learn more.
