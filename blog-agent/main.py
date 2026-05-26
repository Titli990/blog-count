from datetime import datetime

from wordpress import fetch_posts

# Select client
client_name = input("Enter Client Name: ")

# Fetch client posts
posts = fetch_posts(client_name)

# User input
month_input = int(input("Enter Month (1-12): "))
year_input = int(input("Enter Year: "))

# Total blogs
total_blogs = len(posts)

# Filter blogs
filtered_posts = []

for post in posts:

    post_date = post["date"]

    dt = datetime.strptime(post_date, "%Y-%m-%dT%H:%M:%S")

    if dt.month == month_input and dt.year == year_input:
        filtered_posts.append(post)

# Count filtered blogs
filtered_count = len(filtered_posts)

# Month name
month_name = datetime(1900, month_input, 1).strftime('%B')

# Output
print("\n========== BLOG REPORT ==========\n")

print("Client:", client_name)

print("Total Blogs:", total_blogs)

print(f"Blogs Posted In {month_name} {year_input}:",
      filtered_count)