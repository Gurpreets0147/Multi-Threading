import multiprocessing


def data(numbers,q):
   for n in numbers:
      q.put(n)
if __name__ =="__main__":
   num=[1,2,3,4,5,6,7,8,9]
   quee=multiprocessing.Queue()
   proc=multiprocessing.Process(target=data,args=(num,quee))
   proc.start()
   proc.join()
   while quee.empty() is False:
      print (quee.get())
      
