# Giveme5W

Giveme5W is an open-source system to extract answers to the five journalistic W questions (5Ws). The 5Ws describe the main event of a news articles, i.e., who did what, when, where, and why. Giveme5W can be accessed by other software as a Python library and via a RESTful API. The extraction performance is p=0.7.

Note that we currently work on an improved version of Giveme5W, which will be available here very soon.

## Getting started

### Installation
1. Clone the repository
2. Stanford NER: Download version `stanford-ner-2015-12-09` from https://nlp.stanford.edu/software/CRF-NER.shtml#Download (the tool was tested with stanford-ner-2015-12-09, other versions may work as well)
3. Unzip its contents into `/Giveme5W/extractor/resources` (afterward, `/Giveme5W/extractor/resources/stanford-ner-2015-12-09` needs to exist) 
4. `pip3 install -r requirements.txt`

### Use within your own code
If you want to extract the 5Ws from a single article, have a look at the script `examples/fivew_single_article.py`. 
```
$ python3 examples/fivew_single_article.py
```

### Access via RESTful API
Giveme5W provides a RESTful API to which you can send a news article. First, start the server script.
```
$ python3 examples/server.py
```

Starting up the server may take a few moments. Once the server is running, you can send `GET` and `POST` requests to `http://localhost:5000/extract`. You send a single JSON object, that needs to contain at least one of the following fields: 

* `title` 
* `description` (the lead paragraph) 
* `text` (the remainder of the text)

For instance, if your data contains only the headline and the full text of the article, you could send a request containing the headline in the `title` field, and the full text in the `text` field. Giveme5W also supports natively articles extracted by the news crawler and extractor [news-please](https://github.com/fhamborg/news-please).

## How to cite
If you are using Giveme5W, please cite our [paper](http://www.gipp.com/wp-content/papercite-data/pdf/hamborg2018.pdf) ([ResearchGate](https://www.researchgate.net/publication/323582278_Giveme5W_Main_Event_Retrieval_from_News_Articles_by_Extraction_of_the_Five_Journalistic_W_Questions)):
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
