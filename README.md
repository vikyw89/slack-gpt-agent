# Slack Bot

## Overview

This project is a Slack bot built using the `slack-bolt` framework and `FastAPI`. The bot listens for events such as mentions and messages, and responds accordingly.

## Setup

### Prerequisites

- Python 3.12 or higher
- Poetry for dependency management

### Installation

1. Clone the repository.
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

### Configuration

Set the following environment variables in your `.env` file:

```sh
SLACK_SIGNING_SECRET=***
SLACK_CLIENT_ID=111.111
SLACK_CLIENT_SECRET=***
SLACK_SCOPES=app_mentions:read,channels:history,im:history,chat:write
```

### Running the Development Server

To run the development server, use the following command:

```sh
poetry run dev
```

This command will:
- Terminate any process using port 3000.
- Start the FastAPI server using `python -m app.main`.

## Features

### Event Handling

- **App Mentions**: The bot responds with "What's up?" when mentioned.
- **Messages**: The bot currently does not respond to messages.

### API Endpoints

- `/slack/events`: Handles Slack events.
- `/slack/install`: Handles the installation flow for OAuth.
- `/slack/oauth_redirect`: Handles the OAuth redirect.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.