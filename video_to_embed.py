from urllib.parse import urlparse


def clean_url(url, upgrade_https=True):
    the_url = url

    if (not the_url.startswith("http")):
        the_url = "https://" + the_url

    the_url = the_url.replace("://www.", "://")
    the_url = urlparse(the_url, scheme="https")
    # the_url =  the_url._replace(query="")

    if(upgrade_https):
        the_url = the_url._replace(scheme="https")

    return the_url


def video_url_to_embed(url, width=270, height=180):
    the_url = clean_url(url)
    service_name = the_url.netloc
    embed = ""
    src = ""

    # expand youtu.be links
    if(service_name == "youtu.be"):
        the_url = the_url._replace(
            netloc="youtube.com",
            path="/watch",
            query='v=' + the_url.path.replace("/", "")
        )
        service_name = the_url.netloc

    # Find the embed for the service
    if(service_name == "youtube.com"):
        src = f'https://www.youtube-nocookie.com/embed/{the_url.query.replace("v=","")}'
    elif(service_name == "vimeo.com"):
        src = f'https://player.vimeo.com/video/{the_url.path.split("/")[1]}'
    elif(service_name == "dailymotion.com"):
        src = f'https://www.dailymotion.com/embed/video/{the_url.path.split("/")[2]}'
    elif(service_name == "bitchute.com"):
        src = f'https://www.bitchute.com/embed/{the_url.path.split("/")[2]}/'

    embed = f'<iframe width="{width}" height="{height}" src="{src}" frameborder="0" allow="picture-in-picture" allowfullscreen></iframe>'

    print(the_url)
    return embed


examples = [
    "https://youtube.com/watch?v=SDB6f10YPc8",
    "https://youtu.be/CrtuA5HWFoU",
    "https://www.bitchute.com/video/wTA5Vtp5e3I/",
    "https://vimeo.com/67469421",
    "https://www.dailymotion.com/video/x7wsy5j"
]

if __name__ == "__main__":
    string = ""
    with open("test.html", "w+") as f:
        for i in range(3):
            for j in range(3):
                string += video_url_to_embed(examples[i+j]) + "\n"
            string += "<br>\n"
        f.write(string)
