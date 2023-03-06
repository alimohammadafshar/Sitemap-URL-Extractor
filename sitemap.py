import requests
import xmltodict
import openpyxl

# Set the URL of the sitemap
sitemap_url = input('please enter sitemap url in xml format: ')

# Fetch the sitemap XML content
response = requests.get(sitemap_url)
sitemap_xml = response.content

# Parse the XML into a dictionary
sitemap_dict = xmltodict.parse(sitemap_xml)

# Extract the URLs from the sitemap dictionary
urls = []
for urlset in sitemap_dict["urlset"]["url"]:
    urls.append(urlset["loc"])

# Write the URLs to an Excel file
workbook = openpyxl.Workbook()
worksheet = workbook.active
for i, url in enumerate(urls):
    worksheet.cell(row=i+1, column=1, value=url)
workbook.save("urls.xlsx")

# Write the URLs to a TXT file
with open("urls.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")
