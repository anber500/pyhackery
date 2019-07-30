import pika
import uuid
import json

# https://dev.au.swipe.talkingtechportal.com:32672/#/queues/%2F/SWIPEOCallEventDeadLetterQ
#

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
target_exchange = 'TalkingtechExchange'
target_queue = 'SWIPEOCallEventQueue'
channel.exchange_declare(exchange=target_exchange, exchange_type='direct')

message_types = ('SWIPEO.CallRecord', 'SWIPEO.CallStatsRecord',
                 'SWIPEO.CallHistoryRecord')
for message_type in message_types:
    channel.queue_declare(queue=target_queue, durable=True)
    channel.queue_bind(
        exchange=target_exchange, queue=target_queue, routing_key=message_type)

dummy_call_record = """
{
  "CallID": 1039179,
  "CallAt": "2019-06-04T12:37:58.0364082",
  "CallDNIS": null,
  "CallCLID": "021363307",
  "CallPBXD": null,
  "CallMediaType": "VOICE",
  "CallAddress": "021363307",
  "CallPort": null,
  "CallCallDurn": 14.68,
  "CallTalkDurn": 14.68,
  "CallBillDurn": 14.68,
  "CallIsBilled": null,
  "CallIsOutbound": null,
  "CallIsInbound": true,
  "CallContactSuccess": null,
  "CallResult": null,
  "CallResultBase": null,
  "CallAttempt": null,
  "CallApp": "ABC",
  "CallJobID": null,
  "CallWorkID": null,
  "CallWorkPeriodID": null,
  "CallMediaID": null,
  "CallConsumerID": null,
  "CallDestinationID": null,
  "CallQueueN": null,
  "CallGUID": "b6c02bf1-bee6-4b60-8b3e-f8a660f4f973",
  "Client": "Im a CallRecord"
}
"""
"""
json.dumps(({
            'CallGUID': str(uuid.uuid1()),
        }))
"""


def publish_dummy_callrecord_message():
    channel.basic_publish(
        exchange=target_exchange,
        routing_key='SWIPEO.CallRecord',
        body=dummy_call_record)


def publish_dummy_callhistoryrecord_message():
    channel.basic_publish(
        exchange=target_exchange,
        routing_key='SWIPEO.CallHistoryRecord',
        body=json.dumps({
            'CLID': str(uuid.uuid1()),
            'Client': "Im a CallHistoryRecord",
            "CallID": 1234567
        }))


def publish_dummy_callstatsrecord_message(how_many=1):
    def send(identifier):
        channel.basic_publish(
            exchange=target_exchange,
            routing_key='SWIPEO.CallStatsRecord',
            body=json.dumps(({
                'Ivrcallid': identifier,
                'CallID': str(identifier),
                'CallID': str(identifier),
                'Client': "Im a CallStatsRecord"
            })))

    for i in range(how_many):
        send(i)


def publish_dummy_unknowntype_message():
    channel.basic_publish(
        exchange=target_exchange,
        routing_key='I Am An Unknown Type',
        body=json.dumps(({
            'CallID': str(uuid.uuid1()),
            "Client": "Im an unknown type"
        })))


for i in range(1):
    publish_dummy_callrecord_message()
    publish_dummy_callstatsrecord_message(1)
    publish_dummy_callhistoryrecord_message()
    publish_dummy_unknowntype_message()
#  pass
