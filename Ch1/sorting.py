

class Sorting:

    def insertion(self,data):

        for j in range(1,len(data)):
            key = data[j]
            i = j-1

            while (i>-1 and data[i]>key):
                data[i+1] = data[i]
                i = i-1
            
            data[i+1] = key

        