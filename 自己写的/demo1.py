import execjs
import json
with open("123.js","r",encoding="utf-8") as f:
    jscode = f.read()
t = "bOnqtWHqs4t32kZeWEzfoNqIA+aTiXXJK0WUl33PSRHRdOP1Ra6hXvpyOuayBpv/+8PWp6dcAdfLjA5wHhtnmvzviUI8HD7smK1pHMdWEBEpAV0tcEa77aQ7isTpWf2gkv1Zwl9Q6qhtArZahpWrqd8pFZfCVTJr1fGP1MAOWaU7VWL6aSfR1H4aoW/AuJm6mYpFza91XazvbiQVwqL2I7dgj9cMMqITU4KOF+uDw0If7gnaPzn9ZHWCzKZXsHkyx09hbz8xfHJGOGerfZ/3UTBFc1VP9luB8PZHArc4s97Ck7cjXmlc9s1SNnh9/0IyMVxVHT45FHMSHkfbRWOrZzJD/7NwnCGGBExFM1EaUsqYnhIZCt9iCxC3YUxQcc/YyBynN4yeMy54mZGw1YdnfjBLfZsZcQGJHD5plYuZtZzGtT5axTGEc+wFJIOBM9KqAVDP9EjXQbLx0CzDP4mU22ZXuJ8VI2WFomyKq0c1TmXoRIx/YMaDDW732YTvJ5ip9OWZPtfoIxhY3dsgFcXMXJc99avJFFdP8k0WMT2PMz+ir5MJ0eiN6lfXU79AAZgxWgRh5YEpzuhzzIV/hz+44gp6xGS55YblDp1bgfyVHbCq+cJHDHSmxvzviUI8HD7s0iqkrrOZBiSEBMmc+FtEcUNvYUESaJdbOknxv9zQYXQBWXAjhVlAVUuVy/jXrjzbqlhd3bt1v1suwhm+Kz2exc5+hS9LZfPmxnbMKNWSz5vsVCgRqAGpQXs9q9JWuqWTZ5z6syydbD6EBMmc+FtEcThqfYm+nJjcrjlayLajflRw0tRpl9AnyJHN/nJ5ELnF+20gvOmiAz6xIqPbqriBiwp6xGS55YblzJfV4qeU8G93/WUWBMPCkaxKCZlGaFwMFCp8heQuc6iRb1jA68WpXJP6vp74NfYCgxD5WsD5jQgknVUG044HfFesgIYec2QzhrWDvykmb0tYLCPPX67TWi9edT8CdDLRrlqFzRy5W/ZK6XTlbdtONX6hLB2OFGq9+HIqseypV7KXHoBO7n7dTBMrdxLOhJQGSPoL5pj/LI6myDxwsHGYOoX2buu8NvBiL3DQCNKjNj3DcLycA4oSv1dXsk8qipYTCIObMXgn4EYPCZ2IBLLpnCZ5Z1Obg1uUNLDyb68uEl8loUzY7NcsGOMwPFTHxPFm9o+t084ivyeYIWrwLKWa7wALlee5m92J"

ctx = execjs.compile(jscode).call('o',t)
json_data = json.loads(ctx)
print(json_data)

# print(ctx)
