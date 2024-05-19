
import time
import os
import psutil

class UniqueInt:
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        start_time = time.time()
        process = psutil.Process(os.getpid())
        start_memory = process.memory_info().rss / 1024 / 1024

        seen = [False] * 2047

        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()
                if not line or ' ' in line:
                    continue
                try:
                    num = int(line)
                    if num < -1023 or num > 1023:
                        continue
                    seen[num + 1023] = True
                except ValueError:
                    continue

        with open(outputFilePath, 'w') as outputFile:
            for i in range(2047):
                if seen[i]:
                    outputFile.write(f"{i - 1023}\n")

        end_time = time.time()
        end_memory = process.memory_info().rss / 1024 / 1024

        print(f"Runtime: {end_time - start_time} seconds")
        print(f"Memory usage: {end_memory - start_memory} MiB")

        # New code to print the content of the output file
        with open(outputFilePath, 'r') as outputFile:
            print(outputFile.read())

UniqueInt.processFile(r'C:\Users\HP\Downloads\sample_01.txt', r'C:\Users\HP\Downloads\sample_01.txt_result.txt')
