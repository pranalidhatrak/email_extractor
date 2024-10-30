import requests


# This reads the content from a file
def read_file(file_name):
  try:
    f = open(file_name, 'r')
    content = f.read()
    print("Success: File read")
    return content.splitlines()
  except:
    print("Error while reading file")
    return []


# This takes in the content and writes it in a file
def write_file(content, file_name):
  try:
    f = open(file_name, 'w')
    f.write(str(content))
    print("Success: File write")
  except:
    print("Error occured in writing file")


# This takes in a url and returns its HTML code
def fetch(url):
  try:
    response = requests.get(url)
    html = response.text
    return html
  except:
    print("Error in fetching")


# This takes in emails and removes duplicate
def unique_emails(emails):
  email_set = set(emails)
  return list(email_set)


# Function that removes mailto: from the email
def remove_mailto(email):
  return email.replace('mailto:', '')


# This takes in html and returns a list of emails
def extract_emails(html):
  chunk = html.split('"')
  emails = []
  for part in chunk:
    if "mailto:" in part:
      emails.append(remove_mailto(part))
  return unique_emails(emails)


urls = read_file('urls.txt')

emails = []
for url in urls:
  html = fetch(url)
  emails.append(extract_emails(html))

print(emails)

write_file(emails, 'emails.txt')
