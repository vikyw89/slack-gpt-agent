# Slack Bot

## Overview

This project is a Slack bot built using the `slack-bolt` framework, `FastAPI`, `langgraph`. The bot listens for events such as mentions and messages, and responds accordingly.

## Setup

### Prerequisites

- Python 3.11 or higher
- Poetry for dependency management

### Installation

1. Clone the repository.
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

### Configuration

copy .env example and fill all .env

```bash
cp .env.example .env
```

### Running the Development Server

To run the development server, use the following command:

```bash
poetry run dev
```

This command will:

- Terminate any process using port 8000.
- Start the FastAPI server.

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
