# Reddit Subreddit Joiner

This Python script allows you to extract subreddits starting with "r/" from an input file and join those subreddits using the PRAW library. It provides a convenient way to automate the process of subscribing to multiple subreddits on Reddit.

## Prerequisites

Before using this script, you need to have the following:

- Python 3 installed on your machine.
- PRAW (Python Reddit API Wrapper) library installed. You can install it using `pip` with the following command:

    ```bash
    pip install praw
    ```

- Reddit API credentials (client ID and client secret) for authentication purposes. You can obtain these credentials by creating a Reddit script app. Follow these steps to get your credentials:

    1. Go to the [Reddit preferences apps page](https://www.reddit.com/prefs/apps).
    2. Scroll down to the "Developed applications" section and click on the "Create App" or "Create Another App" button.
    3. Fill in the required information for your app (name, description, etc.). Select the "script" option as the app type.
    4. Set the "About URL" and "Redirect URI" fields to any valid URL, as they are not necessary for script-type apps.
    5. Click on the "Create app" button.
    6. On the next page, you will find your client ID and client secret. Take note of these values as they will be needed later.
    
    ![Example](https://i.imgur.com/dT5YExB.jpg)

## Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/reddit-subreddit-joiner.git
    ```

2. Navigate to the project directory:

    ```bash
    cd reddit-subreddit-joiner
    ```

3. Open the script file `reddit_joiner.py` in a text editor.

4. Replace the placeholders with your Reddit API credentials:

    ```python
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    username = "your_username"
    password = "your_password"
    ```

5. Open the 'input.txt' file and paste all the subreddits even it is a whole website containing names of r/ subreddits, it will automatically extract subreddits from that list.

6. Execute the script by running the following command:

    ```bash
    python reddit_joiner.py
    ```

   The script will automatically generate a list of subreddits starting with "r/" from a set of random words and join them using your Reddit API credentials. You will see the output indicating successful join or any errors that occurred during the process.

That's it! You can now easily automate joining multiple subreddits on Reddit using this script.

NOTE : If it found any non-existing subreddit it will ignore those subreddit names and continue to the next subreddits

## License

This project is licensed under the [MIT License](LICENSE).
