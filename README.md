# Giveme5W

Giveme5W is a state of the art open-source 5W Question Answering system for news articles. It can either be used through a simple RESTapi or directly included in existing Python projects. Depending on the configuration Giveme5W parses each document for the answers to the following  questions:

* **Who** is involved?
* **What** happened?
* **Where** did it take place?
* **When** did it happen?
* **Why** did it happen?

## Getting started
Before you can use Giveme5W, you need to make sure you have a CoreNLP-server up and running.
In the case you first to have to install CoreNLP please refer to the CoreNLPs extensive [documentation](https://stanfordnlp.github.io/CoreNLP/corenlp-server.html) and follow the instructions on how to install CoreNLP and start a server.

Starting the CoreNLP server: 
```
$ nohup java -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer 9000 &
```

### (Optional) Configuration
If you are running CoreNLP on a different port or machine you have to first adjust the network settings for the prerpocessor:

(Bsp: extractor/examples/simple_api.py)
```python
# CoreNLP host
core_nlp_host = 'localhost:9000'
```

For the RESTapi it is also possible to network config:
```python
# basic configuration of the rest api
app = Flask(__name__)
log = logging.getLogger(__name__)
host = None
port = 5000
debug = False
options = None
```

You can also adjust the extractors which are used to examine the documents:
```python
# If desired, the selection of extractors can be changed and passed to the FiveWExtractor at initialization
    extractor_list = [
        action_extractor.ActionExtractor(),             # who & what
        environment_extractor.EnvironmentExtractor(),   # when & where
        cause_extractor.CauseExtractor()                # why
    ]
    extractor = FiveWExtractor(preprocessor, extractor_list)
```

### Start the python script
```
$ python extractor/examples/simple_api.py
```

Now you can send articles through the RESTapi to Giveme5W. 
The API supports the following JSON fields:

* title (always required!)
* description
* text

## How to cite
If you are using news-please, please cite our [paper](http://www.gipp.com/wp-content/papercite-data/pdf/hamborg2017.pdf) ([ResearchGate](https://www.researchgate.net/publication/314072045_news-please_A_Generic_News_Crawler_and_Extractor), [Mendeley](https://www.mendeley.com/research-papers/newsplease-generic-news-crawler-extractor/)):
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
