import pika
from pika.adapters.blocking_connection import BlockingChannel


'''
回调函数
'''
def callback(ch: BlockingChannel, method, properties, body: str):
    print(" [x] received %r" % (body,))
    # time.sleep(body.count('.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel  = connection.channel() # 创建channel
queue = channel.queue_declare(queue='task_queue', durable=True) # 创建queue
print("Waiting for messages, To exit press ctrl+c")

channel.basic_consume(callback, queue='task_queue', no_ack=False) # 订阅消息，并确认消息
channel.start_consuming()



