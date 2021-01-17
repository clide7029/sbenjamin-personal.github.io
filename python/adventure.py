


def make_head(title):
    return """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type"text/css" href="styles.css">
    <title>%s</title>
</head>""" % title

def make_page(title):
    head = make_head(branch[])
    html = """<!DOCTYPE html>
<html lang="en">
%s
<body>
    <h1>%s</h1>
    <p>%s</p>
</body>
</html>""" %