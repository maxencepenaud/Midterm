def is_valid_url(url):
    # Check if the URL starts with 'http://' or 'https://'
    return url.startswith("http://") or url.startswith("https://")

# Example usage:
print(is_valid_url("https://www.example.com"))
print(is_valid_url("http://www.example.com"))
print(is_valid_url("www.example.com"))
print(is_valid_url("https://"))
print(is_valid_url("ftp://example.com"))
