# Generated from MyGrammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
<<<<<<< Updated upstream
        4,1,28,196,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,71,8,3,10,3,12,3,74,9,3,1,4,1,4,1,4,3,4,79,8,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,98,8,4,
        10,4,12,4,101,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,112,8,
        5,10,5,12,5,115,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,129,8,6,10,6,12,6,132,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,141,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,151,8,8,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,3,12,167,
        8,12,1,13,1,13,1,13,1,13,3,13,173,8,13,1,14,1,14,1,15,1,15,1,15,
        1,15,3,15,181,8,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,
        3,19,192,8,19,1,20,1,20,1,20,0,5,4,6,8,10,12,21,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,1,1,0,20,22,202,0,42,
        1,0,0,0,2,51,1,0,0,0,4,53,1,0,0,0,6,64,1,0,0,0,8,78,1,0,0,0,10,102,
        1,0,0,0,12,116,1,0,0,0,14,140,1,0,0,0,16,150,1,0,0,0,18,152,1,0,
        0,0,20,156,1,0,0,0,22,159,1,0,0,0,24,166,1,0,0,0,26,172,1,0,0,0,
        28,174,1,0,0,0,30,180,1,0,0,0,32,182,1,0,0,0,34,184,1,0,0,0,36,186,
        1,0,0,0,38,191,1,0,0,0,40,193,1,0,0,0,42,43,3,2,1,0,43,1,1,0,0,0,
        44,45,3,4,2,0,45,46,5,1,0,0,46,52,1,0,0,0,47,48,3,4,2,0,48,49,5,
        1,0,0,49,50,3,2,1,0,50,52,1,0,0,0,51,44,1,0,0,0,51,47,1,0,0,0,52,
        3,1,0,0,0,53,54,6,2,-1,0,54,55,3,6,3,0,55,61,1,0,0,0,56,57,10,2,
        0,0,57,58,5,2,0,0,58,60,3,6,3,0,59,56,1,0,0,0,60,63,1,0,0,0,61,59,
        1,0,0,0,61,62,1,0,0,0,62,5,1,0,0,0,63,61,1,0,0,0,64,65,6,3,-1,0,
        65,66,3,8,4,0,66,72,1,0,0,0,67,68,10,2,0,0,68,69,5,3,0,0,69,71,3,
        8,4,0,70,67,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,
        7,1,0,0,0,74,72,1,0,0,0,75,76,6,4,-1,0,76,79,3,10,5,0,77,79,3,10,
        5,0,78,75,1,0,0,0,78,77,1,0,0,0,79,99,1,0,0,0,80,81,10,8,0,0,81,
        82,5,4,0,0,82,98,3,10,5,0,83,84,10,7,0,0,84,85,5,5,0,0,85,98,3,10,
        5,0,86,87,10,6,0,0,87,88,5,6,0,0,88,98,3,10,5,0,89,90,10,5,0,0,90,
        91,5,7,0,0,91,98,3,10,5,0,92,93,10,4,0,0,93,94,5,8,0,0,94,98,3,10,
        5,0,95,96,10,3,0,0,96,98,5,9,0,0,97,80,1,0,0,0,97,83,1,0,0,0,97,
        86,1,0,0,0,97,89,1,0,0,0,97,92,1,0,0,0,97,95,1,0,0,0,98,101,1,0,
        0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,9,1,0,0,0,101,99,1,0,0,0,102,
        103,6,5,-1,0,103,104,3,12,6,0,104,113,1,0,0,0,105,106,10,3,0,0,106,
        107,5,10,0,0,107,112,3,12,6,0,108,109,10,2,0,0,109,110,5,11,0,0,
        110,112,3,12,6,0,111,105,1,0,0,0,111,108,1,0,0,0,112,115,1,0,0,0,
        113,111,1,0,0,0,113,114,1,0,0,0,114,11,1,0,0,0,115,113,1,0,0,0,116,
        117,6,6,-1,0,117,118,3,14,7,0,118,130,1,0,0,0,119,120,10,4,0,0,120,
        121,5,12,0,0,121,129,3,14,7,0,122,123,10,3,0,0,123,124,5,13,0,0,
        124,129,3,14,7,0,125,126,10,2,0,0,126,127,5,14,0,0,127,129,3,14,
        7,0,128,119,1,0,0,0,128,122,1,0,0,0,128,125,1,0,0,0,129,132,1,0,
        0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,13,1,0,0,0,132,130,1,0,0,
        0,133,134,5,10,0,0,134,141,3,16,8,0,135,136,5,11,0,0,136,141,3,16,
        8,0,137,138,5,15,0,0,138,141,3,16,8,0,139,141,3,16,8,0,140,133,1,
        0,0,0,140,135,1,0,0,0,140,137,1,0,0,0,140,139,1,0,0,0,141,15,1,0,
        0,0,142,143,5,16,0,0,143,144,3,4,2,0,144,145,5,17,0,0,145,151,1,
        0,0,0,146,151,3,18,9,0,147,151,3,20,10,0,148,151,3,22,11,0,149,151,
        3,30,15,0,150,142,1,0,0,0,150,146,1,0,0,0,150,147,1,0,0,0,150,148,
        1,0,0,0,150,149,1,0,0,0,151,17,1,0,0,0,152,153,3,20,10,0,153,154,
        5,18,0,0,154,155,3,10,5,0,155,19,1,0,0,0,156,157,3,24,12,0,157,158,
        3,38,19,0,158,21,1,0,0,0,159,160,3,38,19,0,160,161,5,18,0,0,161,
        162,3,10,5,0,162,23,1,0,0,0,163,164,5,19,0,0,164,167,3,26,13,0,165,
        167,3,26,13,0,166,163,1,0,0,0,166,165,1,0,0,0,167,25,1,0,0,0,168,
        169,3,28,14,0,169,170,5,12,0,0,170,173,1,0,0,0,171,173,3,28,14,0,
        172,168,1,0,0,0,172,171,1,0,0,0,173,27,1,0,0,0,174,175,7,0,0,0,175,
        29,1,0,0,0,176,181,3,32,16,0,177,181,3,34,17,0,178,181,3,36,18,0,
        179,181,3,38,19,0,180,176,1,0,0,0,180,177,1,0,0,0,180,178,1,0,0,
        0,180,179,1,0,0,0,181,31,1,0,0,0,182,183,5,26,0,0,183,33,1,0,0,0,
        184,185,5,27,0,0,185,35,1,0,0,0,186,187,5,25,0,0,187,37,1,0,0,0,
        188,189,5,23,0,0,189,192,3,40,20,0,190,192,3,40,20,0,191,188,1,0,
        0,0,191,190,1,0,0,0,192,39,1,0,0,0,193,194,5,24,0,0,194,41,1,0,0,
        0,16,51,61,72,78,97,99,111,113,128,130,140,150,166,172,180,191
=======
        4,1,43,444,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,127,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,5,2,135,8,2,10,2,12,2,138,9,2,1,3,1,3,1,3,
        1,3,1,3,1,3,5,3,146,8,3,10,3,12,3,149,9,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,
        4,172,8,4,10,4,12,4,175,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,186,8,5,10,5,12,5,189,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,203,8,6,10,6,12,6,206,9,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,215,8,7,1,8,1,8,1,8,1,8,1,8,3,8,222,8,8,1,9,1,9,1,9,
        1,9,3,9,228,8,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,
        239,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        251,8,11,1,12,1,12,1,12,3,12,256,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,265,8,13,1,14,1,14,1,15,1,15,1,15,1,15,3,15,273,8,15,
        1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        3,19,288,8,19,1,20,1,20,1,21,1,21,5,21,294,8,21,10,21,12,21,297,
        9,21,1,21,3,21,300,8,21,1,21,1,21,3,21,304,8,21,1,22,1,22,1,22,1,
        22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,3,27,351,8,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,359,
        8,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,4,29,371,
        8,29,11,29,12,29,372,1,29,4,29,376,8,29,11,29,12,29,377,3,29,380,
        8,29,1,30,1,30,3,30,384,8,30,1,30,1,30,5,30,388,8,30,10,30,12,30,
        391,9,30,1,30,1,30,3,30,395,8,30,1,30,3,30,398,8,30,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,33,1,33,3,33,418,8,33,1,33,5,33,421,8,33,10,33,12,33,424,9,
        33,1,33,1,33,3,33,428,8,33,1,33,3,33,431,8,33,1,34,1,34,1,34,1,34,
        1,34,1,35,1,35,1,36,1,36,1,36,1,36,1,36,0,5,4,6,8,10,12,37,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,0,1,1,0,19,22,469,0,74,1,0,0,
        0,2,126,1,0,0,0,4,128,1,0,0,0,6,139,1,0,0,0,8,150,1,0,0,0,10,176,
        1,0,0,0,12,190,1,0,0,0,14,214,1,0,0,0,16,221,1,0,0,0,18,223,1,0,
        0,0,20,231,1,0,0,0,22,250,1,0,0,0,24,255,1,0,0,0,26,264,1,0,0,0,
        28,266,1,0,0,0,30,272,1,0,0,0,32,274,1,0,0,0,34,276,1,0,0,0,36,278,
        1,0,0,0,38,287,1,0,0,0,40,289,1,0,0,0,42,303,1,0,0,0,44,305,1,0,
        0,0,46,311,1,0,0,0,48,319,1,0,0,0,50,328,1,0,0,0,52,333,1,0,0,0,
        54,341,1,0,0,0,56,365,1,0,0,0,58,379,1,0,0,0,60,397,1,0,0,0,62,399,
        1,0,0,0,64,408,1,0,0,0,66,430,1,0,0,0,68,432,1,0,0,0,70,437,1,0,
        0,0,72,439,1,0,0,0,74,75,3,2,1,0,75,1,1,0,0,0,76,77,3,4,2,0,77,78,
        5,1,0,0,78,127,1,0,0,0,79,80,3,4,2,0,80,81,5,1,0,0,81,82,3,2,1,0,
        82,127,1,0,0,0,83,84,3,58,29,0,84,85,3,2,1,0,85,127,1,0,0,0,86,87,
        3,62,31,0,87,88,3,2,1,0,88,127,1,0,0,0,89,90,3,64,32,0,90,91,3,2,
        1,0,91,127,1,0,0,0,92,93,3,68,34,0,93,94,5,1,0,0,94,95,3,2,1,0,95,
        127,1,0,0,0,96,97,3,18,9,0,97,98,3,2,1,0,98,127,1,0,0,0,99,100,3,
        20,10,0,100,101,5,1,0,0,101,102,3,2,1,0,102,127,1,0,0,0,103,104,
        3,22,11,0,104,105,5,1,0,0,105,106,3,2,1,0,106,127,1,0,0,0,107,108,
        3,44,22,0,108,109,3,2,1,0,109,127,1,0,0,0,110,111,3,56,28,0,111,
        112,3,2,1,0,112,127,1,0,0,0,113,114,3,42,21,0,114,115,3,2,1,0,115,
        127,1,0,0,0,116,117,5,35,0,0,117,118,5,1,0,0,118,127,3,2,1,0,119,
        120,5,36,0,0,120,121,5,1,0,0,121,127,3,2,1,0,122,123,3,72,36,0,123,
        124,3,2,1,0,124,127,1,0,0,0,125,127,1,0,0,0,126,76,1,0,0,0,126,79,
        1,0,0,0,126,83,1,0,0,0,126,86,1,0,0,0,126,89,1,0,0,0,126,92,1,0,
        0,0,126,96,1,0,0,0,126,99,1,0,0,0,126,103,1,0,0,0,126,107,1,0,0,
        0,126,110,1,0,0,0,126,113,1,0,0,0,126,116,1,0,0,0,126,119,1,0,0,
        0,126,122,1,0,0,0,126,125,1,0,0,0,127,3,1,0,0,0,128,129,6,2,-1,0,
        129,130,3,6,3,0,130,136,1,0,0,0,131,132,10,2,0,0,132,133,5,2,0,0,
        133,135,3,6,3,0,134,131,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,
        136,137,1,0,0,0,137,5,1,0,0,0,138,136,1,0,0,0,139,140,6,3,-1,0,140,
        141,3,8,4,0,141,147,1,0,0,0,142,143,10,2,0,0,143,144,5,3,0,0,144,
        146,3,8,4,0,145,142,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,
        148,1,0,0,0,148,7,1,0,0,0,149,147,1,0,0,0,150,151,6,4,-1,0,151,152,
        3,10,5,0,152,173,1,0,0,0,153,154,10,7,0,0,154,155,5,4,0,0,155,172,
        3,10,5,0,156,157,10,6,0,0,157,158,5,5,0,0,158,172,3,10,5,0,159,160,
        10,5,0,0,160,161,5,6,0,0,161,172,3,10,5,0,162,163,10,4,0,0,163,164,
        5,7,0,0,164,172,3,10,5,0,165,166,10,3,0,0,166,167,5,8,0,0,167,172,
        3,10,5,0,168,169,10,2,0,0,169,170,5,9,0,0,170,172,3,10,5,0,171,153,
        1,0,0,0,171,156,1,0,0,0,171,159,1,0,0,0,171,162,1,0,0,0,171,165,
        1,0,0,0,171,168,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,
        1,0,0,0,174,9,1,0,0,0,175,173,1,0,0,0,176,177,6,5,-1,0,177,178,3,
        12,6,0,178,187,1,0,0,0,179,180,10,3,0,0,180,181,5,10,0,0,181,186,
        3,12,6,0,182,183,10,2,0,0,183,184,5,11,0,0,184,186,3,12,6,0,185,
        179,1,0,0,0,185,182,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,
        188,1,0,0,0,188,11,1,0,0,0,189,187,1,0,0,0,190,191,6,6,-1,0,191,
        192,3,14,7,0,192,204,1,0,0,0,193,194,10,4,0,0,194,195,5,33,0,0,195,
        203,3,14,7,0,196,197,10,3,0,0,197,198,5,12,0,0,198,203,3,14,7,0,
        199,200,10,2,0,0,200,201,5,13,0,0,201,203,3,14,7,0,202,193,1,0,0,
        0,202,196,1,0,0,0,202,199,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,
        0,204,205,1,0,0,0,205,13,1,0,0,0,206,204,1,0,0,0,207,208,5,10,0,
        0,208,215,3,16,8,0,209,210,5,11,0,0,210,215,3,16,8,0,211,212,5,14,
        0,0,212,215,3,16,8,0,213,215,3,16,8,0,214,207,1,0,0,0,214,209,1,
        0,0,0,214,211,1,0,0,0,214,213,1,0,0,0,215,15,1,0,0,0,216,217,5,15,
        0,0,217,218,3,4,2,0,218,219,5,16,0,0,219,222,1,0,0,0,220,222,3,30,
        15,0,221,216,1,0,0,0,221,220,1,0,0,0,222,17,1,0,0,0,223,224,3,20,
        10,0,224,227,5,17,0,0,225,228,3,4,2,0,226,228,3,68,34,0,227,225,
        1,0,0,0,227,226,1,0,0,0,228,229,1,0,0,0,229,230,5,1,0,0,230,19,1,
        0,0,0,231,232,3,24,12,0,232,233,3,38,19,0,233,21,1,0,0,0,234,235,
        3,38,19,0,235,238,5,17,0,0,236,239,3,10,5,0,237,239,3,68,34,0,238,
        236,1,0,0,0,238,237,1,0,0,0,239,251,1,0,0,0,240,241,3,30,15,0,241,
        242,5,17,0,0,242,243,3,10,5,0,243,251,1,0,0,0,244,245,5,15,0,0,245,
        246,3,4,2,0,246,247,5,16,0,0,247,248,5,17,0,0,248,249,3,4,2,0,249,
        251,1,0,0,0,250,234,1,0,0,0,250,240,1,0,0,0,250,244,1,0,0,0,251,
        23,1,0,0,0,252,253,5,18,0,0,253,256,3,26,13,0,254,256,3,26,13,0,
        255,252,1,0,0,0,255,254,1,0,0,0,256,25,1,0,0,0,257,258,3,28,14,0,
        258,259,5,33,0,0,259,265,1,0,0,0,260,261,3,28,14,0,261,262,5,34,
        0,0,262,265,1,0,0,0,263,265,3,28,14,0,264,257,1,0,0,0,264,260,1,
        0,0,0,264,263,1,0,0,0,265,27,1,0,0,0,266,267,7,0,0,0,267,29,1,0,
        0,0,268,273,3,32,16,0,269,273,3,34,17,0,270,273,3,36,18,0,271,273,
        3,38,19,0,272,268,1,0,0,0,272,269,1,0,0,0,272,270,1,0,0,0,272,271,
        1,0,0,0,273,31,1,0,0,0,274,275,5,39,0,0,275,33,1,0,0,0,276,277,5,
        40,0,0,277,35,1,0,0,0,278,279,5,38,0,0,279,37,1,0,0,0,280,281,5,
        23,0,0,281,288,3,40,20,0,282,283,5,33,0,0,283,288,3,40,20,0,284,
        285,5,34,0,0,285,288,3,40,20,0,286,288,3,40,20,0,287,280,1,0,0,0,
        287,282,1,0,0,0,287,284,1,0,0,0,287,286,1,0,0,0,288,39,1,0,0,0,289,
        290,5,37,0,0,290,41,1,0,0,0,291,295,3,46,23,0,292,294,3,48,24,0,
        293,292,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,
        296,299,1,0,0,0,297,295,1,0,0,0,298,300,3,50,25,0,299,298,1,0,0,
        0,299,300,1,0,0,0,300,304,1,0,0,0,301,304,3,52,26,0,302,304,3,54,
        27,0,303,291,1,0,0,0,303,301,1,0,0,0,303,302,1,0,0,0,304,43,1,0,
        0,0,305,306,5,24,0,0,306,307,5,15,0,0,307,308,3,4,2,0,308,309,5,
        16,0,0,309,310,5,1,0,0,310,45,1,0,0,0,311,312,5,25,0,0,312,313,5,
        15,0,0,313,314,3,4,2,0,314,315,5,16,0,0,315,316,5,26,0,0,316,317,
        3,70,35,0,317,318,5,27,0,0,318,47,1,0,0,0,319,320,5,28,0,0,320,321,
        5,25,0,0,321,322,5,15,0,0,322,323,3,4,2,0,323,324,5,16,0,0,324,325,
        5,26,0,0,325,326,3,70,35,0,326,327,5,27,0,0,327,49,1,0,0,0,328,329,
        5,28,0,0,329,330,5,26,0,0,330,331,3,70,35,0,331,332,5,27,0,0,332,
        51,1,0,0,0,333,334,5,29,0,0,334,335,5,15,0,0,335,336,3,4,2,0,336,
        337,5,16,0,0,337,338,5,26,0,0,338,339,3,70,35,0,339,340,5,27,0,0,
        340,53,1,0,0,0,341,342,5,30,0,0,342,358,5,15,0,0,343,344,3,20,10,
        0,344,345,5,1,0,0,345,351,1,0,0,0,346,351,3,18,9,0,347,348,3,22,
        11,0,348,349,5,1,0,0,349,351,1,0,0,0,350,343,1,0,0,0,350,346,1,0,
        0,0,350,347,1,0,0,0,351,352,1,0,0,0,352,353,3,4,2,0,353,354,5,1,
        0,0,354,355,3,22,11,0,355,359,1,0,0,0,356,357,5,1,0,0,357,359,5,
        1,0,0,358,350,1,0,0,0,358,356,1,0,0,0,359,360,1,0,0,0,360,361,5,
        16,0,0,361,362,5,26,0,0,362,363,3,70,35,0,363,364,5,27,0,0,364,55,
        1,0,0,0,365,366,5,26,0,0,366,367,3,70,35,0,367,368,5,27,0,0,368,
        57,1,0,0,0,369,371,5,42,0,0,370,369,1,0,0,0,371,372,1,0,0,0,372,
        370,1,0,0,0,372,373,1,0,0,0,373,380,1,0,0,0,374,376,5,41,0,0,375,
        374,1,0,0,0,376,377,1,0,0,0,377,375,1,0,0,0,377,378,1,0,0,0,378,
        380,1,0,0,0,379,370,1,0,0,0,379,375,1,0,0,0,380,59,1,0,0,0,381,383,
        3,24,12,0,382,384,5,37,0,0,383,382,1,0,0,0,383,384,1,0,0,0,384,385,
        1,0,0,0,385,386,5,31,0,0,386,388,1,0,0,0,387,381,1,0,0,0,388,391,
        1,0,0,0,389,387,1,0,0,0,389,390,1,0,0,0,390,392,1,0,0,0,391,389,
        1,0,0,0,392,394,3,24,12,0,393,395,5,37,0,0,394,393,1,0,0,0,394,395,
        1,0,0,0,395,398,1,0,0,0,396,398,1,0,0,0,397,389,1,0,0,0,397,396,
        1,0,0,0,398,61,1,0,0,0,399,400,3,24,12,0,400,401,5,37,0,0,401,402,
        5,15,0,0,402,403,3,60,30,0,403,404,5,16,0,0,404,405,5,26,0,0,405,
        406,3,70,35,0,406,407,5,27,0,0,407,63,1,0,0,0,408,409,3,24,12,0,
        409,410,5,37,0,0,410,411,5,15,0,0,411,412,3,60,30,0,412,413,5,16,
        0,0,413,414,5,1,0,0,414,65,1,0,0,0,415,418,5,37,0,0,416,418,3,30,
        15,0,417,415,1,0,0,0,417,416,1,0,0,0,418,419,1,0,0,0,419,421,5,31,
        0,0,420,417,1,0,0,0,421,424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,
        0,0,423,427,1,0,0,0,424,422,1,0,0,0,425,428,5,37,0,0,426,428,3,30,
        15,0,427,425,1,0,0,0,427,426,1,0,0,0,428,431,1,0,0,0,429,431,1,0,
        0,0,430,422,1,0,0,0,430,429,1,0,0,0,431,67,1,0,0,0,432,433,5,37,
        0,0,433,434,5,15,0,0,434,435,3,66,33,0,435,436,5,16,0,0,436,69,1,
        0,0,0,437,438,3,2,1,0,438,71,1,0,0,0,439,440,5,32,0,0,440,441,3,
        4,2,0,441,442,5,1,0,0,442,73,1,0,0,0,34,126,136,147,171,173,185,
        187,202,204,214,221,227,238,250,255,264,272,287,295,299,303,350,
        358,372,377,379,383,389,394,397,417,422,427,430
>>>>>>> Stashed changes
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'&&'", "'||'", "'=='", "'<='", 
<<<<<<< Updated upstream
                     "'>='", "'!='", "'<'", "'>'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'('", "')'", "'='", "'const'", 
                     "'int'", "'float'", "'char'", "'&'" ]
=======
                     "'>='", "'!='", "'<'", "'>'", "'+'", "'-'", "'/'", 
                     "'%'", "'!'", "'('", "')'", "'='", "'const'", "'int'", 
                     "'float'", "'char'", "'void'", "'&'", "'printf'", "'if'", 
                     "'{'", "'}'", "'else'", "'while'", "'for'", "','", 
                     "'return'", "'*'", "<INVALID>", "'break'", "'continue'" ]
>>>>>>> Stashed changes

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
<<<<<<< Updated upstream
                      "ID", "CHAR", "INT", "FLOAT", "WS" ]
=======
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "POINTER", "POINTERS", "BREAK", "CONTINUE", 
                      "ID", "CHAR", "INT", "FLOAT", "COMMENT", "BLOCK_COMMENT", 
                      "WS" ]
>>>>>>> Stashed changes

    RULE_prog = 0
    RULE_expr = 1
    RULE_opAnd = 2
    RULE_opOr = 3
    RULE_opCompare = 4
    RULE_opAddOrSub = 5
    RULE_opMultOrDiv = 6
    RULE_opUnary = 7
    RULE_brackets = 8
    RULE_variableDefinition = 9
    RULE_variableDeclaration = 10
    RULE_assignmentStatement = 11
    RULE_constWord = 12
    RULE_pointerWord = 13
    RULE_reservedWord = 14
    RULE_dataTypes = 15
    RULE_int = 16
    RULE_float = 17
    RULE_char = 18
    RULE_referenceID = 19
    RULE_nameIdentifier = 20
<<<<<<< Updated upstream
=======
    RULE_conditionStatement = 21
    RULE_printFunction = 22
    RULE_ifStatement = 23
    RULE_elifStatement = 24
    RULE_elseStatement = 25
    RULE_whileStatement = 26
    RULE_forLoop = 27
    RULE_unNamedScope = 28
    RULE_comment = 29
    RULE_argument = 30
    RULE_funcDefinition = 31
    RULE_funcDeclaration = 32
    RULE_argumentCall = 33
    RULE_functionCall = 34
    RULE_body = 35
    RULE_returnStatement = 36
>>>>>>> Stashed changes

    ruleNames =  [ "prog", "expr", "opAnd", "opOr", "opCompare", "opAddOrSub", 
                   "opMultOrDiv", "opUnary", "brackets", "variableDefinition", 
                   "variableDeclaration", "assignmentStatement", "constWord", 
                   "pointerWord", "reservedWord", "dataTypes", "int", "float", 
<<<<<<< Updated upstream
                   "char", "referenceID", "nameIdentifier" ]
=======
                   "char", "referenceID", "nameIdentifier", "conditionStatement", 
                   "printFunction", "ifStatement", "elifStatement", "elseStatement", 
                   "whileStatement", "forLoop", "unNamedScope", "comment", 
                   "argument", "funcDefinition", "funcDeclaration", "argumentCall", 
                   "functionCall", "body", "returnStatement" ]
>>>>>>> Stashed changes

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
<<<<<<< Updated upstream
    ID=24
    CHAR=25
    INT=26
    FLOAT=27
    WS=28
=======
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    POINTER=33
    POINTERS=34
    BREAK=35
    CONTINUE=36
    ID=37
    CHAR=38
    INT=39
    FLOAT=40
    COMMENT=41
    BLOCK_COMMENT=42
    WS=43
>>>>>>> Stashed changes

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MyGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 42
=======
            self.state = 74
>>>>>>> Stashed changes
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


<<<<<<< Updated upstream
=======
        def comment(self):
            return self.getTypedRuleContext(MyGrammarParser.CommentContext,0)


        def funcDefinition(self):
            return self.getTypedRuleContext(MyGrammarParser.FuncDefinitionContext,0)


        def funcDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.FuncDeclarationContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MyGrammarParser.FunctionCallContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDefinitionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.AssignmentStatementContext,0)


        def printFunction(self):
            return self.getTypedRuleContext(MyGrammarParser.PrintFunctionContext,0)


        def unNamedScope(self):
            return self.getTypedRuleContext(MyGrammarParser.UnNamedScopeContext,0)


        def conditionStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.ConditionStatementContext,0)


        def BREAK(self):
            return self.getToken(MyGrammarParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MyGrammarParser.CONTINUE, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.ReturnStatementContext,0)


>>>>>>> Stashed changes
        def getRuleIndex(self):
            return MyGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = MyGrammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
<<<<<<< Updated upstream
            self.state = 51
=======
            self.state = 126
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 44
                self.opAnd(0)
                self.state = 45
=======
                self.state = 76
                self.opAnd(0)
                self.state = 77
>>>>>>> Stashed changes
                self.match(MyGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
<<<<<<< Updated upstream
                self.state = 47
                self.opAnd(0)
                self.state = 48
                self.match(MyGrammarParser.T__0)
                self.state = 49
                self.expr()
                pass

=======
                self.state = 79
                self.opAnd(0)
                self.state = 80
                self.match(MyGrammarParser.T__0)
                self.state = 81
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.comment()
                self.state = 84
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.funcDefinition()
                self.state = 87
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.funcDeclaration()
                self.state = 90
                self.expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.functionCall()
                self.state = 93
                self.match(MyGrammarParser.T__0)
                self.state = 94
                self.expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 96
                self.variableDefinition()
                self.state = 97
                self.expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 99
                self.variableDeclaration()
                self.state = 100
                self.match(MyGrammarParser.T__0)
                self.state = 101
                self.expr()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 103
                self.assignmentStatement()
                self.state = 104
                self.match(MyGrammarParser.T__0)
                self.state = 105
                self.expr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 107
                self.printFunction()
                self.state = 108
                self.expr()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 110
                self.unNamedScope()
                self.state = 111
                self.expr()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 113
                self.conditionStatement()
                self.state = 114
                self.expr()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 116
                self.match(MyGrammarParser.BREAK)
                self.state = 117
                self.match(MyGrammarParser.T__0)
                self.state = 118
                self.expr()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 119
                self.match(MyGrammarParser.CONTINUE)
                self.state = 120
                self.match(MyGrammarParser.T__0)
                self.state = 121
                self.expr()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 122
                self.returnStatement()
                self.state = 123
                self.expr()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)

                pass

>>>>>>> Stashed changes

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opOr(self):
            return self.getTypedRuleContext(MyGrammarParser.OpOrContext,0)


        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAnd" ):
                listener.enterOpAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAnd" ):
                listener.exitOpAnd(self)



    def opAnd(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpAndContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_opAnd, _p)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 54
            self.opOr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 61
=======
            self.state = 129
            self.opOr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 136
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opAnd)
<<<<<<< Updated upstream
                    self.state = 56
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 57
                    self.match(MyGrammarParser.T__1)
                    self.state = 58
                    self.opOr(0) 
                self.state = 63
=======
                    self.state = 131
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 132
                    self.match(MyGrammarParser.T__1)
                    self.state = 133
                    self.opOr(0) 
                self.state = 138
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opCompare(self):
            return self.getTypedRuleContext(MyGrammarParser.OpCompareContext,0)


        def opOr(self):
            return self.getTypedRuleContext(MyGrammarParser.OpOrContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpOr" ):
                listener.enterOpOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpOr" ):
                listener.exitOpOr(self)



    def opOr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpOrContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_opOr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 65
            self.opCompare(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 72
=======
            self.state = 140
            self.opCompare(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpOrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opOr)
<<<<<<< Updated upstream
                    self.state = 67
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 68
                    self.match(MyGrammarParser.T__2)
                    self.state = 69
                    self.opCompare(0) 
                self.state = 74
=======
                    self.state = 142
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 143
                    self.match(MyGrammarParser.T__2)
                    self.state = 144
                    self.opCompare(0) 
                self.state = 149
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpCompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


        def opCompare(self):
            return self.getTypedRuleContext(MyGrammarParser.OpCompareContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opCompare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpCompare" ):
                listener.enterOpCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpCompare" ):
                listener.exitOpCompare(self)



    def opCompare(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpCompareContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_opCompare, _p)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 76
                self.opAddOrSub(0)
                pass

            elif la_ == 2:
                self.state = 77
                self.opAddOrSub(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 99
=======
            self.state = 151
            self.opAddOrSub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 173
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
<<<<<<< Updated upstream
                    self.state = 97
=======
                    self.state = 171
>>>>>>> Stashed changes
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
<<<<<<< Updated upstream
                        self.state = 80
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 81
                        self.match(MyGrammarParser.T__3)
                        self.state = 82
=======
                        self.state = 153
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 154
                        self.match(MyGrammarParser.T__3)
                        self.state = 155
>>>>>>> Stashed changes
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
<<<<<<< Updated upstream
                        self.state = 83
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 84
                        self.match(MyGrammarParser.T__4)
                        self.state = 85
=======
                        self.state = 156
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 157
                        self.match(MyGrammarParser.T__4)
                        self.state = 158
>>>>>>> Stashed changes
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
<<<<<<< Updated upstream
                        self.state = 86
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 87
                        self.match(MyGrammarParser.T__5)
                        self.state = 88
=======
                        self.state = 159
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 160
                        self.match(MyGrammarParser.T__5)
                        self.state = 161
>>>>>>> Stashed changes
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
<<<<<<< Updated upstream
                        self.state = 89
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 90
                        self.match(MyGrammarParser.T__6)
                        self.state = 91
=======
                        self.state = 162
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 163
                        self.match(MyGrammarParser.T__6)
                        self.state = 164
>>>>>>> Stashed changes
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
<<<<<<< Updated upstream
                        self.state = 92
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 93
                        self.match(MyGrammarParser.T__7)
                        self.state = 94
=======
                        self.state = 165
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 166
                        self.match(MyGrammarParser.T__7)
                        self.state = 167
>>>>>>> Stashed changes
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
<<<<<<< Updated upstream
                        self.state = 95
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 96
                        self.match(MyGrammarParser.T__8)
                        pass

             
                self.state = 101
=======
                        self.state = 168
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 169
                        self.match(MyGrammarParser.T__8)
                        self.state = 170
                        self.opAddOrSub(0)
                        pass

             
                self.state = 175
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpAddOrSubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opMultOrDiv(self):
            return self.getTypedRuleContext(MyGrammarParser.OpMultOrDivContext,0)


        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opAddOrSub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAddOrSub" ):
                listener.enterOpAddOrSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAddOrSub" ):
                listener.exitOpAddOrSub(self)



    def opAddOrSub(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpAddOrSubContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_opAddOrSub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 103
            self.opMultOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 113
=======
            self.state = 177
            self.opMultOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 187
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
<<<<<<< Updated upstream
                    self.state = 111
=======
                    self.state = 185
>>>>>>> Stashed changes
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
<<<<<<< Updated upstream
                        self.state = 105
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 106
                        self.match(MyGrammarParser.T__9)
                        self.state = 107
=======
                        self.state = 179
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 180
                        self.match(MyGrammarParser.T__9)
                        self.state = 181
>>>>>>> Stashed changes
                        self.opMultOrDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
<<<<<<< Updated upstream
                        self.state = 108
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 109
                        self.match(MyGrammarParser.T__10)
                        self.state = 110
=======
                        self.state = 182
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 183
                        self.match(MyGrammarParser.T__10)
                        self.state = 184
>>>>>>> Stashed changes
                        self.opMultOrDiv(0)
                        pass

             
<<<<<<< Updated upstream
                self.state = 115
=======
                self.state = 189
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpMultOrDivContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opUnary(self):
            return self.getTypedRuleContext(MyGrammarParser.OpUnaryContext,0)


        def opMultOrDiv(self):
            return self.getTypedRuleContext(MyGrammarParser.OpMultOrDivContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opMultOrDiv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMultOrDiv" ):
                listener.enterOpMultOrDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMultOrDiv" ):
                listener.exitOpMultOrDiv(self)



    def opMultOrDiv(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.OpMultOrDivContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_opMultOrDiv, _p)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 117
            self.opUnary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 130
=======
            self.state = 191
            self.opUnary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
<<<<<<< Updated upstream
                    self.state = 128
=======
                    self.state = 202
>>>>>>> Stashed changes
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
<<<<<<< Updated upstream
                        self.state = 119
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 120
                        self.match(MyGrammarParser.T__11)
                        self.state = 121
=======
                        self.state = 193
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 194
                        self.match(MyGrammarParser.POINTER)
                        self.state = 195
>>>>>>> Stashed changes
                        self.opUnary()
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
<<<<<<< Updated upstream
                        self.state = 122
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 123
                        self.match(MyGrammarParser.T__12)
                        self.state = 124
=======
                        self.state = 196
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 197
                        self.match(MyGrammarParser.T__11)
                        self.state = 198
>>>>>>> Stashed changes
                        self.opUnary()
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
<<<<<<< Updated upstream
                        self.state = 125
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 126
                        self.match(MyGrammarParser.T__13)
                        self.state = 127
=======
                        self.state = 199
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 200
                        self.match(MyGrammarParser.T__12)
                        self.state = 201
>>>>>>> Stashed changes
                        self.opUnary()
                        pass

             
<<<<<<< Updated upstream
                self.state = 132
=======
                self.state = 206
>>>>>>> Stashed changes
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OpUnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def brackets(self):
            return self.getTypedRuleContext(MyGrammarParser.BracketsContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_opUnary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpUnary" ):
                listener.enterOpUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpUnary" ):
                listener.exitOpUnary(self)




    def opUnary(self):

        localctx = MyGrammarParser.OpUnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opUnary)
        try:
<<<<<<< Updated upstream
            self.state = 140
=======
            self.state = 214
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 133
                self.match(MyGrammarParser.T__9)
                self.state = 134
=======
                self.state = 207
                self.match(MyGrammarParser.T__9)
                self.state = 208
>>>>>>> Stashed changes
                self.brackets()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
<<<<<<< Updated upstream
                self.state = 135
                self.match(MyGrammarParser.T__10)
                self.state = 136
=======
                self.state = 209
                self.match(MyGrammarParser.T__10)
                self.state = 210
>>>>>>> Stashed changes
                self.brackets()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
<<<<<<< Updated upstream
                self.state = 137
                self.match(MyGrammarParser.T__14)
                self.state = 138
                self.brackets()
                pass
            elif token in [16, 19, 20, 21, 22, 23, 24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
=======
                self.state = 211
                self.match(MyGrammarParser.T__13)
                self.state = 212
                self.brackets()
                pass
            elif token in [15, 23, 33, 34, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
>>>>>>> Stashed changes
                self.brackets()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BracketsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDefinitionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDeclarationContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.AssignmentStatementContext,0)


        def dataTypes(self):
            return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_brackets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)




    def brackets(self):

        localctx = MyGrammarParser.BracketsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_brackets)
        try:
<<<<<<< Updated upstream
            self.state = 150
=======
            self.state = 221
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 142
=======
                self.state = 216
                self.match(MyGrammarParser.T__14)
                self.state = 217
                self.opAnd(0)
                self.state = 218
>>>>>>> Stashed changes
                self.match(MyGrammarParser.T__15)
                self.state = 143
                self.opAnd(0)
                self.state = 144
                self.match(MyGrammarParser.T__16)
                pass
<<<<<<< Updated upstream

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.variableDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.variableDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.assignmentStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
=======
            elif token in [23, 33, 34, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
>>>>>>> Stashed changes
                self.dataTypes()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDeclarationContext,0)


        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MyGrammarParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)




    def variableDefinition(self):

        localctx = MyGrammarParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 152
            self.variableDeclaration()
            self.state = 153
            self.match(MyGrammarParser.T__17)
            self.state = 154
            self.opAddOrSub(0)
=======
            self.state = 223
            self.variableDeclaration()
            self.state = 224
            self.match(MyGrammarParser.T__16)
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 225
                self.opAnd(0)
                pass

            elif la_ == 2:
                self.state = 226
                self.functionCall()
                pass


            self.state = 229
            self.match(MyGrammarParser.T__0)
>>>>>>> Stashed changes
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ConstWordContext,0)


        def referenceID(self):
            return self.getTypedRuleContext(MyGrammarParser.ReferenceIDContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = MyGrammarParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 156
            self.constWord()
            self.state = 157
=======
            self.state = 231
            self.constWord()
            self.state = 232
>>>>>>> Stashed changes
            self.referenceID()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def referenceID(self):
            return self.getTypedRuleContext(MyGrammarParser.ReferenceIDContext,0)


        def opAddOrSub(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAddOrSubContext,0)


<<<<<<< Updated upstream
=======
        def functionCall(self):
            return self.getTypedRuleContext(MyGrammarParser.FunctionCallContext,0)


        def dataTypes(self):
            return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,0)


        def opAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.OpAndContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.OpAndContext,i)


>>>>>>> Stashed changes
        def getRuleIndex(self):
            return MyGrammarParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = MyGrammarParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignmentStatement)
        try:
<<<<<<< Updated upstream
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.referenceID()
            self.state = 160
            self.match(MyGrammarParser.T__17)
            self.state = 161
            self.opAddOrSub(0)
=======
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.referenceID()
                self.state = 235
                self.match(MyGrammarParser.T__16)
                self.state = 238
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 236
                    self.opAddOrSub(0)
                    pass

                elif la_ == 2:
                    self.state = 237
                    self.functionCall()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.dataTypes()
                self.state = 241
                self.match(MyGrammarParser.T__16)
                self.state = 242
                self.opAddOrSub(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.match(MyGrammarParser.T__14)
                self.state = 245
                self.opAnd(0)
                self.state = 246
                self.match(MyGrammarParser.T__15)
                self.state = 247
                self.match(MyGrammarParser.T__16)
                self.state = 248
                self.opAnd(0)
                pass


>>>>>>> Stashed changes
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointerWord(self):
            return self.getTypedRuleContext(MyGrammarParser.PointerWordContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_constWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstWord" ):
                listener.enterConstWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstWord" ):
                listener.exitConstWord(self)




    def constWord(self):

        localctx = MyGrammarParser.ConstWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constWord)
        try:
<<<<<<< Updated upstream
            self.state = 166
=======
            self.state = 255
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 163
                self.match(MyGrammarParser.T__18)
                self.state = 164
                self.pointerWord()
                pass
            elif token in [20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
=======
                self.state = 252
                self.match(MyGrammarParser.T__17)
                self.state = 253
                self.pointerWord()
                pass
            elif token in [19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
>>>>>>> Stashed changes
                self.pointerWord()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reservedWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ReservedWordContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_pointerWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerWord" ):
                listener.enterPointerWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerWord" ):
                listener.exitPointerWord(self)




    def pointerWord(self):

        localctx = MyGrammarParser.PointerWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_pointerWord)
        try:
<<<<<<< Updated upstream
            self.state = 172
=======
            self.state = 264
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 168
                self.reservedWord()
                self.state = 169
                self.match(MyGrammarParser.T__11)
=======
                self.state = 257
                self.reservedWord()
                self.state = 258
                self.match(MyGrammarParser.POINTER)
>>>>>>> Stashed changes
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
<<<<<<< Updated upstream
                self.state = 171
=======
                self.state = 260
                self.reservedWord()
                self.state = 261
                self.match(MyGrammarParser.POINTERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
>>>>>>> Stashed changes
                self.reservedWord()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReservedWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_reservedWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReservedWord" ):
                listener.enterReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReservedWord" ):
                listener.exitReservedWord(self)




    def reservedWord(self):

        localctx = MyGrammarParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_reservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
=======
            self.state = 266
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
>>>>>>> Stashed changes
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self):
            return self.getTypedRuleContext(MyGrammarParser.IntContext,0)


        def float_(self):
            return self.getTypedRuleContext(MyGrammarParser.FloatContext,0)


        def char(self):
            return self.getTypedRuleContext(MyGrammarParser.CharContext,0)


        def referenceID(self):
            return self.getTypedRuleContext(MyGrammarParser.ReferenceIDContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_dataTypes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataTypes" ):
                listener.enterDataTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataTypes" ):
                listener.exitDataTypes(self)




    def dataTypes(self):

        localctx = MyGrammarParser.DataTypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dataTypes)
        try:
<<<<<<< Updated upstream
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.int_()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.float_()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.char()
                pass
            elif token in [23, 24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
=======
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.int_()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.float_()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.char()
                pass
            elif token in [23, 33, 34, 37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
>>>>>>> Stashed changes
                self.referenceID()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = MyGrammarParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 182
=======
            self.state = 274
>>>>>>> Stashed changes
            self.match(MyGrammarParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(MyGrammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = MyGrammarParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 184
=======
            self.state = 276
>>>>>>> Stashed changes
            self.match(MyGrammarParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(MyGrammarParser.CHAR, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)




    def char(self):

        localctx = MyGrammarParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 186
=======
            self.state = 278
>>>>>>> Stashed changes
            self.match(MyGrammarParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameIdentifier(self):
            return self.getTypedRuleContext(MyGrammarParser.NameIdentifierContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_referenceID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenceID" ):
                listener.enterReferenceID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenceID" ):
                listener.exitReferenceID(self)




    def referenceID(self):

        localctx = MyGrammarParser.ReferenceIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_referenceID)
        try:
<<<<<<< Updated upstream
            self.state = 191
=======
            self.state = 287
>>>>>>> Stashed changes
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
                self.state = 188
                self.match(MyGrammarParser.T__22)
                self.state = 189
                self.nameIdentifier()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
=======
                self.state = 280
                self.match(MyGrammarParser.T__22)
                self.state = 281
                self.nameIdentifier()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(MyGrammarParser.POINTER)
                self.state = 283
                self.nameIdentifier()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.match(MyGrammarParser.POINTERS)
                self.state = 285
                self.nameIdentifier()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
>>>>>>> Stashed changes
                self.nameIdentifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_nameIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameIdentifier" ):
                listener.enterNameIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameIdentifier" ):
                listener.exitNameIdentifier(self)




    def nameIdentifier(self):

        localctx = MyGrammarParser.NameIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_nameIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
<<<<<<< Updated upstream
            self.state = 193
=======
            self.state = 289
>>>>>>> Stashed changes
            self.match(MyGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.opAnd_sempred
        self._predicates[3] = self.opOr_sempred
        self._predicates[4] = self.opCompare_sempred
        self._predicates[5] = self.opAddOrSub_sempred
        self._predicates[6] = self.opMultOrDiv_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def opAnd_sempred(self, localctx:OpAndContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def opOr_sempred(self, localctx:OpOrContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def opCompare_sempred(self, localctx:OpCompareContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

<<<<<<< Updated upstream
            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         
=======
        def whileStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.WhileStatementContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MyGrammarParser.ForLoopContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_conditionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionStatement" ):
                listener.enterConditionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionStatement" ):
                listener.exitConditionStatement(self)




    def conditionStatement(self):

        localctx = MyGrammarParser.ConditionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_conditionStatement)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.ifStatement()
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 292
                        self.elifStatement() 
                    self.state = 297
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==28:
                    self.state = 298
                    self.elseStatement()


                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.whileStatement()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.forLoop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_printFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFunction" ):
                listener.enterPrintFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFunction" ):
                listener.exitPrintFunction(self)




    def printFunction(self):

        localctx = MyGrammarParser.PrintFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_printFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MyGrammarParser.T__23)
            self.state = 306
            self.match(MyGrammarParser.T__14)
            self.state = 307
            self.opAnd(0)
            self.state = 308
            self.match(MyGrammarParser.T__15)
            self.state = 309
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def body(self):
            return self.getTypedRuleContext(MyGrammarParser.BodyContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = MyGrammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(MyGrammarParser.T__24)
            self.state = 312
            self.match(MyGrammarParser.T__14)
            self.state = 313
            self.opAnd(0)
            self.state = 314
            self.match(MyGrammarParser.T__15)
            self.state = 315
            self.match(MyGrammarParser.T__25)
            self.state = 316
            self.body()
            self.state = 317
            self.match(MyGrammarParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def body(self):
            return self.getTypedRuleContext(MyGrammarParser.BodyContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_elifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifStatement" ):
                listener.enterElifStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifStatement" ):
                listener.exitElifStatement(self)




    def elifStatement(self):

        localctx = MyGrammarParser.ElifStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(MyGrammarParser.T__27)
            self.state = 320
            self.match(MyGrammarParser.T__24)
            self.state = 321
            self.match(MyGrammarParser.T__14)
            self.state = 322
            self.opAnd(0)
            self.state = 323
            self.match(MyGrammarParser.T__15)
            self.state = 324
            self.match(MyGrammarParser.T__25)
            self.state = 325
            self.body()
            self.state = 326
            self.match(MyGrammarParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(MyGrammarParser.BodyContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_elseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStatement" ):
                listener.enterElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStatement" ):
                listener.exitElseStatement(self)




    def elseStatement(self):

        localctx = MyGrammarParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(MyGrammarParser.T__27)
            self.state = 329
            self.match(MyGrammarParser.T__25)
            self.state = 330
            self.body()
            self.state = 331
            self.match(MyGrammarParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def body(self):
            return self.getTypedRuleContext(MyGrammarParser.BodyContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = MyGrammarParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MyGrammarParser.T__28)
            self.state = 334
            self.match(MyGrammarParser.T__14)
            self.state = 335
            self.opAnd(0)
            self.state = 336
            self.match(MyGrammarParser.T__15)
            self.state = 337
            self.match(MyGrammarParser.T__25)
            self.state = 338
            self.body()
            self.state = 339
            self.match(MyGrammarParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(MyGrammarParser.BodyContext,0)


        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def assignmentStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.AssignmentStatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.AssignmentStatementContext,i)


        def variableDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDeclarationContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDefinitionContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = MyGrammarParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(MyGrammarParser.T__29)
            self.state = 342
            self.match(MyGrammarParser.T__14)
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 18, 19, 20, 21, 22, 23, 33, 34, 37, 38, 39, 40]:
                self.state = 350
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 343
                    self.variableDeclaration()
                    self.state = 344
                    self.match(MyGrammarParser.T__0)
                    pass

                elif la_ == 2:
                    self.state = 346
                    self.variableDefinition()
                    pass

                elif la_ == 3:
                    self.state = 347
                    self.assignmentStatement()
                    self.state = 348
                    self.match(MyGrammarParser.T__0)
                    pass


                self.state = 352
                self.opAnd(0)
                self.state = 353
                self.match(MyGrammarParser.T__0)
                self.state = 354
                self.assignmentStatement()
                pass
            elif token in [1]:
                self.state = 356
                self.match(MyGrammarParser.T__0)
                self.state = 357
                self.match(MyGrammarParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 360
            self.match(MyGrammarParser.T__15)
            self.state = 361
            self.match(MyGrammarParser.T__25)
            self.state = 362
            self.body()
            self.state = 363
            self.match(MyGrammarParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnNamedScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(MyGrammarParser.BodyContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_unNamedScope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnNamedScope" ):
                listener.enterUnNamedScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnNamedScope" ):
                listener.exitUnNamedScope(self)




    def unNamedScope(self):

        localctx = MyGrammarParser.UnNamedScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unNamedScope)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MyGrammarParser.T__25)
            self.state = 366
            self.body()
            self.state = 367
            self.match(MyGrammarParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.BLOCK_COMMENT)
            else:
                return self.getToken(MyGrammarParser.BLOCK_COMMENT, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.COMMENT)
            else:
                return self.getToken(MyGrammarParser.COMMENT, i)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = MyGrammarParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_comment)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 369
                        self.match(MyGrammarParser.BLOCK_COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 372 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 374
                        self.match(MyGrammarParser.COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 377 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constWord(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ConstWordContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ConstWordContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.ID)
            else:
                return self.getToken(MyGrammarParser.ID, i)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = MyGrammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 397
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 381
                        self.constWord()
                        self.state = 383
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==37:
                            self.state = 382
                            self.match(MyGrammarParser.ID)


                        self.state = 385
                        self.match(MyGrammarParser.T__30) 
                    self.state = 391
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.state = 392
                self.constWord()
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 393
                    self.match(MyGrammarParser.ID)


                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ConstWordContext,0)


        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def argument(self):
            return self.getTypedRuleContext(MyGrammarParser.ArgumentContext,0)


        def body(self):
            return self.getTypedRuleContext(MyGrammarParser.BodyContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_funcDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDefinition" ):
                listener.enterFuncDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDefinition" ):
                listener.exitFuncDefinition(self)




    def funcDefinition(self):

        localctx = MyGrammarParser.FuncDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.constWord()
            self.state = 400
            self.match(MyGrammarParser.ID)
            self.state = 401
            self.match(MyGrammarParser.T__14)
            self.state = 402
            self.argument()
            self.state = 403
            self.match(MyGrammarParser.T__15)
            self.state = 404
            self.match(MyGrammarParser.T__25)
            self.state = 405
            self.body()
            self.state = 406
            self.match(MyGrammarParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ConstWordContext,0)


        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def argument(self):
            return self.getTypedRuleContext(MyGrammarParser.ArgumentContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_funcDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDeclaration" ):
                listener.enterFuncDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDeclaration" ):
                listener.exitFuncDeclaration(self)




    def funcDeclaration(self):

        localctx = MyGrammarParser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_funcDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.constWord()
            self.state = 409
            self.match(MyGrammarParser.ID)
            self.state = 410
            self.match(MyGrammarParser.T__14)
            self.state = 411
            self.argument()
            self.state = 412
            self.match(MyGrammarParser.T__15)
            self.state = 413
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.ID)
            else:
                return self.getToken(MyGrammarParser.ID, i)

        def dataTypes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.DataTypesContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_argumentCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentCall" ):
                listener.enterArgumentCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentCall" ):
                listener.exitArgumentCall(self)




    def argumentCall(self):

        localctx = MyGrammarParser.ArgumentCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_argumentCall)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 33, 34, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 417
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                        if la_ == 1:
                            self.state = 415
                            self.match(MyGrammarParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 416
                            self.dataTypes()
                            pass


                        self.state = 419
                        self.match(MyGrammarParser.T__30) 
                    self.state = 424
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                self.state = 427
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 425
                    self.match(MyGrammarParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 426
                    self.dataTypes()
                    pass


                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def argumentCall(self):
            return self.getTypedRuleContext(MyGrammarParser.ArgumentCallContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = MyGrammarParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MyGrammarParser.ID)
            self.state = 433
            self.match(MyGrammarParser.T__14)
            self.state = 434
            self.argumentCall()
            self.state = 435
            self.match(MyGrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = MyGrammarParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = MyGrammarParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(MyGrammarParser.T__31)
            self.state = 440
            self.opAnd(0)
            self.state = 441
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.opAnd_sempred
        self._predicates[3] = self.opOr_sempred
        self._predicates[4] = self.opCompare_sempred
        self._predicates[5] = self.opAddOrSub_sempred
        self._predicates[6] = self.opMultOrDiv_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def opAnd_sempred(self, localctx:OpAndContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def opOr_sempred(self, localctx:OpOrContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def opCompare_sempred(self, localctx:OpCompareContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         
>>>>>>> Stashed changes

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

    def opAddOrSub_sempred(self, localctx:OpAddOrSubContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def opMultOrDiv_sempred(self, localctx:OpMultOrDivContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




