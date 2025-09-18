log_file = "access.log"  # Replace with your log file

not_found_count = 0
most_requested_pages = {}

with open(log_file, "r") as file:
    for line in file:
        if " 404 " in line:
            not_found_count += 1
        parts = line.split()
        if len(parts) > 6:  #the requested URL is in the 7th column
            page = parts[6]
            most_requested_pages[page] = most_requested_pages.get(page, 0) + 1

print(f"Total 404 Errors: {not_found_count}")

# Most requested page
if most_requested_pages:
    page = max(most_requested_pages, key=most_requested_pages.get)
    print(f"Most requested page: {page} ({most_requested_pages[page]} requests)")
