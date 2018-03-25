import logging
from flask import Flask, request, jsonify

from extractor.document import Document
from extractor.five_w_extractor import FiveWExtractor

app = Flask(__name__)
log = logging.getLogger(__name__)
host = None
port = 5000
debug = False
options = None
extractor = FiveWExtractor()
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)
log.setLevel(logging.DEBUG)


def run():
    log.info("starting server on port %i", port)
    app.run(host, port, debug)
    log.info("server has stopped")


@app.route('/extract', methods=['GET', 'POST'])
def extract():
    json_article = request.get_json()
    if not json_article:
        log.warning("received no article")
        return jsonify({"error": "no article defined"})
    
    article = {}
    if json_article.get('title'):
        article['title'] = json_article.get('title')
        article['description'] = json_article.get('description')
        article['text'] = json_article.get('text')
    else:
        article['title'] = json_article['articletext']
        article['description'] = None
        article['text'] = None
    
    log.debug("retrieved raw article for extraction: %s", json_article['title'])
    
    document = Document(article['title'], article['description'], article['text'])
    extractor.parse(document)

    return jsonify(document.questions)


if __name__ == "__main__":
    run()
