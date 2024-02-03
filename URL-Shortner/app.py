import pyshorteners

def short_url(url):
    shortener = pyshorteners.Shortener()
    a = shortener.tinyurl.short(url)
    return a

url_data = "https://www.google.com/search?gs_ssp=eJzj4tTP1TdIrygzyzNg9OJLzCstzshOVCjOSC0pqQQAd_QJPQ&q=anushka+shetty&rlz=1C1CHBF_enIN1079IN1079&oq=Anushka&gs_lcrp=EgZjaHJvbWUqDQgDEC4YgwEYsQMYgAQyDQgAEAAY4wIYsQMYgAQyCggBEC4YsQMYgAQyBggCEEUYOTINCAMQLhiDARixAxiABDINCAQQLhiDARixAxiABDINCAUQLhiDARixAxiABDIKCAYQABixAxiABDIKCAcQABixAxiABDIKCAgQABixAxiABDIKCAkQABixAxiABNIBCjEwODY2ajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8"
print(short_url(url_data))