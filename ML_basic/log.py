import logging

'''
1、debug 调试级别的日志
2、info  信息级别的日志
3、warning  警告级别的日志
4、error    错误级别的日志
'''
# logging.basicConfig=(filename='my.log',level=logging.DEBUG,format=LOG_format)
# logging.debug('this is a debug log')
# logging.info('this is a info log')
# logging.warning('this is a warning log')
# logging.error('this is a error log')



logger=logging.getLogger()
logger.setLevel('DEBUG')
#文件处理器，输入到文件
file_handler=logging.FileHandler('ml.log',mode='a',encoding='UTF-8')
#流处理器，控制输入到控制台
stream_handler=logging.StreamHandler()
#错误日志单独输出到一个文件
error_handler=logging.fileHandler('error.log',mode='a', encoding='UTF-8')
error_handler.setLevel(logging.ERROR)

#将所有的处理器添加到logger中
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.addHandler(error_handler)
