import aiml
k = aiml.Kernel()
k.learn('std-startup.xml')
k.respond('load aiml b')#'std-startup的模式匹配'
while True:
    print(k.respond(input('input>>'))) #对话的循环