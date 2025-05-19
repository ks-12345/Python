import pyshorteners as ps

url = input("Digite sua URL: ")

u = ps.Shortener().tinyur.short(url)

print("URL: ", u)
