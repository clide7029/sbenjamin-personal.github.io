


adv_page2A = {
    "title"   : "page2a",
    "content" : "ready for an adventure?",
    "pathA"   : "go down this path",
    "pathB"   : "or maybe this one",
    # "pathA"   : ("go down this path", adv_page3A),
    # "pathB"   : ("or maybe this one", adv_page3B)
}
adv_page2B = {
    "title"   : "page2b",
    "content" : "you died",
    "pathA"   : "go down this path",
    "pathB"   : "or maybe this one"
    # "pathA"   : ("go down this path", adv_page3C),
    # "pathB"   : ("or maybe this one", adv_page3D)
}
adv_page1 = {
    "title"   : "page1",
    "content" : "you are here for an adventure",
    "pathA"   : ("go down this path", adv_page2A["title"]),
    "pathB"   : ("or maybe this one", adv_page2B["title"])
}

adventure = [adv_page1, adv_page2A, adv_page2B]

def make_page(adv_page):
    buttonA = adv_page["pathA"]
    labelA = buttonA[0]
    linkA = buttonA[1] + ".html"
    buttonB = adv_page["pathB"]
    labelB = buttonB[0]
    linkB = buttonB[1] + ".html"
    html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="style.css">
        <title>%s</title>
    </head>

    <body>
        <div class="headSpace"></div>
        <div class="container">
            <h1>%s</h1>
            <p>%s</p>
            <div class="centerButtons">
                <button> <a href="%s"> %s </a></button>
                <button> <a href="%s"> %s </a></button>
            </div>
        </div>
    </body>
    </html>
    """ % (adv_page["title"], adv_page["title"], adv_page["content"], 
        linkA, labelA, linkB, labelB)

    f = open(adv_page["title"] + ".html","w")
    f.write(html)
    f.close()

for page in adventure:
    make_page(page)


    # <div class="container">
    #         <h1>%s</h1>
    #         <p>%s</p>
    #         <div class="centerButtons">
    #             <div class="button"> <a href="%s"> %s </a></div>
    #             <div class="button"> <a href="%s"> %s </a></div>
    #         </div>
    #     </div>