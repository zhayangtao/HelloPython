class FileFaker:
    def write(self, string):
        pass
print('s', file=FileFaker())

x = 'keller rabbit'
if x == 'roger':
    print("how's jessica?")
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away!')

# 消息队列
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello') # 创建queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] sent 'hello world!'")

connection.close()