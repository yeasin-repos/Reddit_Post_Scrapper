import praw
import tkinter as tk
from tkinter import ttk

def get_new_posts(client_id, client_secret, username, password, subreddit_name):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         user_agent="Reddit client by u/" + username)
    subreddit = reddit.subreddit(subreddit_name)
    post_titles = []

    for post in subreddit.new(limit=10):  # Limit to 10 posts
        post_titles.append(post.title)

    return post_titles

def fetch_data():
    client_id = client_id_entry.get()
    client_secret = client_secret_entry.get()
    username = username_entry.get()
    subreddit_name = subreddit_entry.get()

    post_titles = get_new_posts(client_id, client_secret, username, subreddit_name)
    post_list.delete(0, tk.END)  # Clear previous entries
    for title in post_titles:
        post_list.insert(tk.END, title)

# Create main window
root = tk.Tk()
root.title("Reddit Post Fetcher")
root.configure(bg="#bb9cc0")

# Client ID Entry
client_id_label = ttk.Label(root, text="Client ID:", background="#bb9cc0")
client_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
client_id_entry = ttk.Entry(root, width=50)
client_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Client Secret Entry
client_secret_label = ttk.Label(root, text="Client Secret:", background="#bb9cc0")
client_secret_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
client_secret_entry = ttk.Entry(root, width=50)
client_secret_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Username Entry
username_label = ttk.Label(root, text="Username:", background="#bb9cc0")
username_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
username_entry = ttk.Entry(root, width=50)
username_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Subreddit Entry
subreddit_label = ttk.Label(root, text="Subreddit:", background="#bb9cc0")
subreddit_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
subreddit_entry = ttk.Entry(root, width=50)
subreddit_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Fetch Data Button
fetch_button = ttk.Button(root, text="Fetch Posts", command=fetch_data, style="Fetch.TButton")
fetch_button.grid(row=5, column=0, columnspan=2, pady=10)

# Post List
post_list = tk.Listbox(root, width=80, height=15, bg="#ffffff", fg="#000000")
post_list.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Configure style
style = ttk.Style(root)
style.configure("TButton", background="#bb9cc0", foreground="#000000")
style.map("TButton",
          background=[("active", "#7d349b")],
          foreground=[("active", "#000000")])

root.mainloop()
