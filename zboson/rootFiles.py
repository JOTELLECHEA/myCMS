import sys

if len(sys.argv) > 1:
    print('Printing Files from',sys.argv[1],'to',sys.argv[2])

else:
    print('No Arguments Passed.')

start = int(sys.argv[1])
end = int(sys.argv[2])
file = open('data/CMS_Run2015D_DoubleEG_MINIAOD_08Jun2016-v1_10000_file_index.txt')

lines = file.readlines()

lineCount = int(len(lines))

for i in range(start - 1 ,end):
	print(lines[i].strip())

