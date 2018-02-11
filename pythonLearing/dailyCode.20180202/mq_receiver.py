import pika

'''
回调函数
'''
def callback(ch, method, properties, body):
    print(" [x] received %r" % (body,))

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel  = connection.channel() # 创建channel
queue = channel.queue_declare(queue='hello') # 创建queue
channel.basic_consume(callback, queue='hello', no_ack=True) # 订阅消息
print("Waiting for messages, To exit press ctrl+c")
channel.start_consuming()



