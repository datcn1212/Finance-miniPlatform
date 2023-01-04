from kafka import KafkaConsumer

consumer = KafkaConsumer('dat')

for msg in consumer:
    print (msg)