# reference:https://github.com/melvilgit/external-Merge-Sort

 import os
import tempfile
import heapq
import sys
import fileinput
import glob
import asyncio

file_list = glob.glob('unsorted*.txt') 

with open('unsorted', 'w') as file:
    for file_name in file_list:
        f = open( file_name , 'r' )
        content = f.read().strip()
        f.close()
        file.write((content))
        file.write("\n")

class heapnode:
    

    def __init__(
            self,
            item,
            fileHandler,
    ):
        self.item = item
        self.fileHandler = fileHandler


class externalMergeSort:


    def __init__(self):
        self.sortedTempFileHandlerList = []
        self.getCurrentDir()

    def getCurrentDir(self):
        self.cwd = os.getcwd()

 

    def iterateSortedData(self, sortedCompleteData):
        for no in sortedCompleteData:
            print (no)

   

    def mergeSortedtempFiles(self):
        mergedNo = (map(int, tempFileHandler) for tempFileHandler in
                    self.sortedTempFileHandlerList)  
        sortedCompleteData = heapq.merge(
            *mergedNo)  
        return sortedCompleteData



    def heapify(
            self,
            arr,
            i,
            n,
    ):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left].item < arr[i].item:
            smallest = left
        else:
            smallest = i

        if right < n and arr[right].item < arr[smallest].item:
            smallest = right

        if i != smallest:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest, n)

    

    def construct_heap(self, arr):
        l = len(arr) - 1
        mid = int(l / 2)
        while mid >= 0:
            self.heapify(arr, mid, l)
            mid -= 1

  
    def mergeSortedtempFiles_low_level(self):
        list = []
        sorted_output = [] 
        for tempFileHandler in self.sortedTempFileHandlerList:
            item = int(tempFileHandler.readline().strip())
            list.append(heapnode(item, tempFileHandler))

        self.construct_heap(list)
        while True:
            min = list[0]
            if min.item == sys.maxsize:
                break
            sorted_output.append(min.item)
            fileHandler = min.fileHandler
            item = fileHandler.readline().strip()
            if not item:
                item = sys.maxsize
            else:
                item = int(item)
            list[0] = heapnode(item, fileHandler)
            self.heapify(list, 0, len(list))
         
        return sorted_output

  

    def splitFiles(self, largeFileName, smallFileSize):
        largeFileHandler = open(largeFileName,'rb')
        tempBuffer = []
        size = 0
        while True:
            number = largeFileHandler.readline()
            if not number:
                break
            tempBuffer.append(number)
            size += 1
            if size % smallFileSize == 0:
                tempBuffer = sorted(tempBuffer, key=lambda no: \
                    int(no.strip()))
                tempFile = tempfile.NamedTemporaryFile(dir=self.cwd + '/temp' , delete=False)
                tempFile.writelines(tempBuffer)
                tempFile.seek(0)
                self.sortedTempFileHandlerList.append(tempFile)
                tempBuffer = []


async def main():
   
    largeFileName = "unsorted"
    smallFileSize = 10
    obj = externalMergeSort()
    obj.splitFiles(largeFileName, smallFileSize)
    await asyncio.sleep(1)
    arr = obj.mergeSortedtempFiles_low_level()
    for x in arr:
     print (x)

if __name__ == '__main__':
     asyncio.run(main())

  
   
