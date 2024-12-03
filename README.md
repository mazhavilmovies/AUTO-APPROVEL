# MN Bot

A feature-rich Telegram bot with:
- **MongoDB Database** integration.
- **Force Subscribe** for restricted access.
- **Broadcast Feature** for mass messaging.
- **Detailed Logs** for user activities and join requests.

## Features

- `/start`: Greet users and display bot usage.
- Join request approval with logging.
- `/stats`: Show user and group stats.
- **Force Subscribe** for restricted access.
- Log details when a user starts the bot and when join requests are accepted.

## Installation

### Prerequisites

Before installing, make sure you have the following:

- Python 3.7 or higher
- MongoDB instance (you can use MongoDB Atlas or any MongoDB server)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/mn-bot.git
    cd mn-bot
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your `.env` file**:

    Copy the `.env.example` file to `.env` and fill in your details:
    ```bash
    cp .env.example .env
    ```

    Update `.env` with your own values for:

    - `BOT_TOKEN`: The token you got from @BotFather on Telegram.
    - `API_ID` and `API_HASH`: Your Telegram API credentials (get them from [here](https://my.telegram.org/auth)).
    - `LOG_CHANNEL_ID`: The ID of the log channel for logging user activity.
    - `JOIN_REQUEST_LOG_CHANNEL_ID`: The ID of the channel where join request approvals are logged.
    - `MONGO_URI`: Your MongoDB connection string (MongoDB Atlas or a local instance).

    Example `.env` file:
    ```env
    BOT_TOKEN=your_bot_token
    API_ID=your_api_id
    API_HASH=your_api_hash
    LOG_CHANNEL_ID=-1001234567890
    JOIN_REQUEST_LOG_CHANNEL_ID=-1009876543210
    MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/mn-bot?retryWrites=true&w=majority
    ```

5. **Run the bot**:
    ```bash
    python app.py
    ```

## Deploy

You can deploy this bot on any cloud platform like:
- **Heroku**
- **Render**
- **Koyeb**

### Deployment Steps (Example with Heroku)

1. **Create a new Heroku application**.
2. **Add your MongoDB URI to Heroku environment variables**:
    - Go to your Heroku app’s settings.
    - Add the `MONGO_URI` variable.
    - Set your bot token, API ID, and API Hash as environment variables in the same way.
3. **Push your repository to Heroku**:
    ```bash
    git remote add heroku https://git.heroku.com/your-heroku-app.git
    git push heroku main
    ```

4. **Scale your dynos**:
    ```bash
    heroku ps:scale web=1
    ```

The bot should now be running on Heroku.

## Usage

Once the bot is running, you can interact with it using the following commands:

- `/start`: Greet users and display bot usage.
- `/stats`: Displays statistics about the bot's usage (number of users, groups, and channels).

When a user interacts with the bot, it will check if they are subscribed to the required channels. If they are not, the bot will send an invite link to the required channel(s).

## MongoDB Integration

The bot uses MongoDB to store user and chat data. It tracks:

- **User Details**: User ID, name, username, and interaction data.
- **Chat Details**: Information about channels or groups where the bot is active.

## Logs

The bot sends logs to two separate channels:

1. **User Activity Log**: When a user starts the bot, their details are logged.
2. **Join Request Log**: When a join request is approved, the details of the user and the chat are logged.

## Code Structure

- **app.py**: Main file where the bot runs and handles commands and events.
- **config.py**: Stores configuration and credentials.
- **utils/db.py**: MongoDB database handler.
- **utils/helpers.py**: Helper functions for logging, greeting, and managing users.
- **.env**: Stores sensitive information like tokens and database URI.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

