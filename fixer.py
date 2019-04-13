import re
import logging

# Set up logging
LOG_FORMAT = "%(name)s %(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger(__name__)
logger.info("Logger is at level: {}".format(logger.level))

# Set up variables
    # retime- regular expression fto find the time element of a post
    # regname- regular expression to find the name element of a post
    # inputpath- input file path
    # outputpath- output file path
    # name- username of person who posted the post
regtime = '\[([0-9]|0[0-9]|1[0-9]):[0-5][0-9]\s((AM)|(PM))\]'
regname = '^(.*?):'
inputpath = '_input.txt'
outputpath = '_output.txt'
name = ''
logger.debug("Local input path: {}  Local output path: {}".format(inputpath, outputpath))

# Open the input and output files
with open(inputpath, 'r') as i:
    with open(outputpath, 'w') as o:
        lines = i.readlines()
        for j in range(len(lines) - 1):
            match = re.match(regtime, lines[j])
            if match is not None:
                logger.debug("Matched: {}".format(match))
                lines[j] = lines[j].replace(match.group(0), '')
        for j in range(len(lines) - 1):
            line1 = lines[j]
            line2 = lines[j + 1]
            logger.debug("\n j: {}\nj+1: {}\n".format(lines[j], lines[j+1]))
            match = re.match(regname, line1)
            if match is not None:
                name = match.group(0)
            if re.match(regname, line2):
                lines[j + 1] = lines[j + 1].replace(name, '')

        o.writelines(lines)
