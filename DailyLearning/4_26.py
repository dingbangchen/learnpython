# f = open('out.txt','w')
# L = []
# for ser_num in range(9,17):
#     for node_num in range(1,13):
#         break
# for switch_node in range(1,49):
#     break
# print(ser_num,node_num,switch_node)





# for switch_num in range(15,17):
#     for switch_node in range(1,49):
#                 print(ser_num,"-",node_num,"<>IPMI-",switch_num,"-",switch_node,sep="",file=f)

from multiprocessing import Process
def loop_a():
   for ser_num in range(9,17):
       for node_num in range(1,13):
           print(ser_num,node_num)

def loop_b():
    for switch_node in range(1,49):
        print(switch_node)
loop_a()
loop_b()