from google.cloud import language

from google.cloud import pubsub

#publisher = pubsub.PublisherClient()

def language_analysis(text):
    client = pubsub.PublisherClient()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    sentiment = sent_analysis.sentiment
    ent_analysis = document.analyze_entities()
    entities = ent_analysis.entities

    return sentiment,entities

example = 'Python is a ver good programming language'

entities = language_analysis(example)

for e in entities:
    print(e.name,e.salience)
