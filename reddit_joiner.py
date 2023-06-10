import praw

# Set up your PRAW credentials
reddit = praw.Reddit(
    user_agent="mass sub",
    client_id="your_client_id",
    client_secret="your_client_secret",
    username="your_username",
    password="your_password"
)

input_file = "input.txt"  # Replace with the path to your input file
output_file = "output.txt"  # Replace with the path where you want to save the output file

# Step 1: Extract subreddits starting with "r/" from the input file

with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

matches = []

# Iterate over each line and find words starting with "r/"
for line in lines:
    if line.startswith("r/"):
        line_matches = [word for word in line.split() if word.startswith("r/")]
        matches.extend(line_matches)

# Join the matched words with newlines
matched_words = "\n".join(matches)

with open(output_file, "w", encoding="utf-8") as file:
    file.write(matched_words)

print("Isolated words starting with 'r/' have been saved to", output_file)

# Step 2: Join subreddits using PRAW

with open(output_file, "r") as file:
    subreddits = [line.strip() for line in file.readlines()]

for subreddit_name in subreddits:
    print("Line: {}".format(subreddit_name))
    try:
        reddit.subreddit(subreddit_name).subscribe()
        print("Subreddit '{}' joined successfully.".format(subreddit_name))
    except praw.exceptions.RedditAPIException as e:
        print("Error joining subreddit '{}': {}".format(subreddit_name, e))
    except Exception as e:
        print("An error occurred while processing subreddit '{}': {}".format(subreddit_name, e))
