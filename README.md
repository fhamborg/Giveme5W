# Giveme5W

Giveme5W is an open-source system to extract answers to the five journalistic W questions (5Ws). The 5Ws describe the main event of a news articles, i.e., who did what, when, where, and why. Giveme5W can be accessed by other software as a Python library and via a RESTful API. The extraction performance is p=0.7.

Note that we currently work on an improved version of Giveme5W, which will be available here very soon.

## Getting started

### Installation
The following steps setup Giveme5W on a Linux system. If you are using MacOS, see the [installation wiki](https://github.com/fhamborg/Giveme5W/wiki/Installation). 
1. Clone the repository
2. Stanford NER: Download version `stanford-ner-2015-12-09` from the [Stanford NER website](https://nlp.stanford.edu/software/CRF-NER.shtml#Download) (the tool was tested with stanford-ner-2015-12-09, other versions may work as well)
3. Unzip its contents into `/Giveme5W/extractor/resources` (afterward, `/Giveme5W/extractor/resources/stanford-ner-2015-12-09` needs to exist) 
4. `pip3 install -r requirements.txt`

### Use within your own code
Invoking Giveme5W is straightforward - it only requires a couple of lines of codes, and Giveme5W takes care of the rest! If you want to extract the 5Ws from a single article, run the following code.
```
from extractor.document import Document
from extractor.five_w_extractor import FiveWExtractor

extractor = FiveWExtractor()

document = Document(articletext)
extractor.parse(document)
```
Note that while Giveme5W allows you to just put in an article's whole text (including or excluding the headline), you can also separately pass the headline, lead paragraph (which we call description), and main text.
```
document = Document(title, description, text)
```

Afterward, you can access the questions and their answers, e.g.:
```
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(document.questions)
```

### Example script
Giveme5W also includes an example [script](https://github.com/fhamborg/Giveme5W/blob/master/examples/fivew_single_article.py) that can runs out of the box.
```
$ python3 examples/fivew_single_article.py
```

### Access via RESTful API
Giveme5W provides a RESTful API to which you can send a news article. First, start the server script.
```
$ python3 examples/server.py
```

Starting up the server may take a few moments. Once the server is running, you can send `GET` and `POST` requests to `http://localhost:5000/extract`. You can send a single JSON object that needs to contain the text of an article, i.e., a field named 

* `articletext` (the text of the article including or excluding the headline)

Alternatively, you can also distinctively send the headline, lead paragraph, and the full text:

* `title` 
* `description` (the lead paragraph) 
* `text` (the remainder of the text)

Giveme5W supports natively articles extracted by our news crawler and extractor [news-please](https://github.com/fhamborg/news-please).

## How to cite
If you are using Giveme5W, please cite our [paper](http://www.gipp.com/wp-content/papercite-data/pdf/hamborg2018.pdf) ([ResearchGate](https://www.researchgate.net/publication/323582278_Giveme5W_Main_Event_Retrieval_from_News_Articles_by_Extraction_of_the_Five_Journalistic_W_Questions), [Mendeley](https://www.mendeley.com/research-papers/giveme5w-main-event-retrieval-news-articles-extraction-five-journalistic-w-questions/?utm_source=desktop&utm_medium=1.17.13&utm_campaign=open_catalog&userDocumentId=%7B6945b48b-a775-4b85-b09b-f321b316f6da%7D)):
```
@InProceedings{Hamborg2018,
  author    = {Hamborg, Felix and Lachnit, Soeren and Schubotz, Moritz and Hepp, Thomas and Gipp, Bela},
  title     = {Giveme5W: Main Event Retrieval from News Articles by Extraction of the Five Journalistic W Questions},
  booktitle = {Proceedings of the iConference 2018},
  year      = {2018},
  month     = {March},
  location  = {Sheffield, UK}
}
```
You can find more information on this and other news projects on our [website](https://felix.hamborg.eu/).

## Contribution and support
Do you want to contribute? Great, we are always happy for any support on this project! Just send a pull request. By contributing to this project, you agree that your contributions will be licensed under the project's license (see below). If you have questions or issues while working on the code, e.g., when implementing a new feature that you would like to have added to Giveme5W, open an issue on GitHub and we'll be happy to help you. Please note that we usually do not have enough resources to implement features requested by users - instead we recommend to implement them yourself, and send a pull request. 

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use Giveme5W except in compliance with the License. A copy of the License is included in the project, see the file [LICENSE.txt](LICENSE.txt).

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 

Copyright 2017-2018 The Giveme5W team
