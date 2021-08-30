# Jokess Slack Bot

Jokess Bot is a simple slack bot to send automated scheduled jokes to slack channels

## Setup

### Prerequisite

1. Python 3.X.X
2. Requests
3. Slack SDK

### Running Locally

For running locally, Please create a virtual environment and install the dependencies in that environment.

```bash
python -m venv env
```

### Create a Slack App

1. Visit [Slack API](https://api.slack.com/apps).
2. Click on **Create App**.
3. Select **From Scratch**.
4. Enter your **App Name** & **Workspace**. This can be changed later.
5. Choose **Bots** as Feature and Functionality.
6. Then assign a scope to your bot token, You will be redirected to the scope page. scroll down to **Bot Token Scopes**.
7. Scopes you need to add : channels:read, chat:write, chat:write.customize, chat:write.public, im:write, mpim:write
8. Go to **OAuth & Permissions** and Search for **OAuth Tokens for Your Workspace**.
9. Copy your token and use it the below command

### Heroku Setup

1. Login to your Heroku Dashboard.
2. create a pipeline and an application on Heroku platform and upload your code to it.
3. You can use Heroku CLI or GitHub to connect your source code to Heroku application
4. Then you can go into Deploy menu in the Heroku application and deploy the application. It will install the required packages in the environment and ready the python environment for your app.
5. Now you have to create the scheduler for your python script. To do that, you can use Heroku add-ons. Go to resources menu in your Heroku application and search for **Heroku Scheduler** (Free Option).
6. Enter the config as per your requirement and add this command - `python app.py --channel=<CHANNEL> --token=<TOKEN>`

### Testing Heroku Scheduler

1. Download the Heroku CLI.
2. Run `heroku login -i`.
3. Enter **Email** and **Password**.
4. Run the following command to check the scheduled task/job - `heroku run python app.py --channel=<CHANNEL> --token=<TOKEN> --app <APP NAME>`

### Environment Variables (Optional)

Jokess variables can also be added to environment variables as follows

```bash
export JOKESS_BOT_CHANNEL=<CHANNEL>
export JOKESS_BOT_AUTH_TOKEN=<TOKEN>
```

## Command

```bash
python3 app.py --channel=<CHANNEL> --token=<TOKEN>
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Icons

Icons made by [Freepik](https://www.freepik.com) from [www.flaticon.com](https://www.flaticon.com/)