# 消息队列
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello') # 创建queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] sent 'hello world!'")

connection.close()