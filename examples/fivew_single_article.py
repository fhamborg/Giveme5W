import logging
import pprint

from extractor.document import Document
from extractor.five_w_extractor import FiveWExtractor

extractor = FiveWExtractor()
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)
log.setLevel(logging.DEBUG)
pp = pprint.PrettyPrinter(indent=4)

article = {}
article['title'] = "Moscow to Kiev: Stick to Minsk ceasefire, stop making false 'invasion' claims"
article['description'] = "Russia has called on Ukraine to stick to the Minsk peace process and disproved claims that Russia is deploying additional troops on the border. Kiev has again accused Russia of invading Ukraine, but has not produced any proof."
article['text'] = """The calls from Russia come as tension is rising in eastern Ukraine, and rebels say Kiev is preparing to break the ceasefire and resume hostilities.

Amid the threat of escalation, Russia is calling for a new round of talks in the Belarusian capital, Minsk.

“We call for the Minsk process to continue and for a new gathering of the contact group,” Russian presidential adviser Yury Ushakov said Friday.

Negotiations in Minsk managed to produce a shaky ceasefire in early September, which has mostly held until now. They didn’t stop the violence altogether, as some flare-ups occurred on the border between areas controlled by Kiev loyalists and rebel forces, such as the fighting over the ruins of Donetsk international airport. But the violence was reduced.

The calls come after Ukrainian Prime Minister Arseniy Yatsenyuk called this week to abandon the Minsk talks altogether and go back to the Geneva negotiations format from April. Unlike the Kiev talks, the talks in Geneva did not include representatives of the rebel forces.

“Sitting [down] with them for bilateral negotiations is useless,” Yatsenyuk said. “One of the most efficient and real formats is the Geneva format, which included the participation of the US, the EU, Ukraine and our geographically northern neighbor.” 

 The “northern neighbor,” as the Ukrainian PM referred to Russia, argued that the agreement that the Geneva format produced in April failed to stop the violence, because Ukraine never even started to implement the accord and instead of the political reform the agreement called for, sent its troops to shell rebel cities.

The exchange comes as amid expectations of a possible resumption of hostilities in Eastern Ukraine. Rebels reported a large build-up of Ukrainian troops near the separation line and said they expected a massive attack at any time. Kiev said the allegations were lies.

The rebels have good reasons to suspect foul play from Kiev, considering that a number of high-ranking Ukrainian officials have stated that use of force in the east was needed. The latest statement came Thursday from Markiyan Lubkivskiy, an aide to the head of Ukraine’s Security Service.

“I believe that sooner or later we will have to start very active actions,” he said on Shuster Live, Ukraine’s main TV talk show on politics.

Earlier, Yury Lutsenko, an aide to Ukrainian President Petro Poroshenko, said Kiev’s interest in the ceasefire was to win time to regroup its troops.

“We need to maintain the ceasefire as long as we can to get our precise instruments, to get military and financial aid from the West,” he said last month. “We are the ones benefiting from the ceasefire and peace.”

Ukrainian servicemen ride on armoured vehicles near Slaviansk (Reuters / Gleb Garanich)

Accusations of an escalation of tensions have also come this week from Kiev. On Friday a spokesman for the anti-rebel campaign, Andrey Lysenko, claimed that Russia has sent 32 tanks, 16 howitzers, 30 trucks of ammunition and three trucks with radar equipment to rebel-held areas. He offered no evidence of his claim, however.

Kiev has also accused Russia of deploying additional troops along its border with Ukraine this week. The reports even prompted Canadian Foreign Minister John Baird to condemn Russia on Wednesday.

“We strongly condemn these provocative actions by Russia, and we believe this is further proof that the Kremlin only seeks to hamper the peace process in Ukraine,” Baird said in a statement.

This provoked a sarcastic response from the Russia Defense Ministry, which said the reports were not true and that Canada should address its concerns to those producing the rumors, rather than to Russia.

“All such provocative ‘reports’ aimed at further escalating the tension over the civil conflict in southeast Ukraine have a single source. The source is not Ukrainian, although it currently operates from one of the governmental buildings in Kiev,” the statement said, apparently alleging to the heavy presence of American personnel in the Ukrainian Security Service.

Tensions in Eastern Ukraine are also on the rise after the self-proclaimed Donetsk and Lugansk People’s Republics held elections last week.

Ukraine and its sponsors branded the ballot an irrelevant mockery and a violation of the Minsk agreement. Russia said it respected the choice of the people living in the breakaway regions, but stopped short of formally recognizing them, a move that Washington said would lead to further economic sanctions against Russia. """

document = Document(article['title'], article['description'], article['text'])
extractor.parse(document)

pp.pprint(document.questions)
