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
        4,1,52,565,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,160,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,168,8,2,10,2,12,
        2,171,9,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,179,8,3,10,3,12,3,182,9,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,5,4,205,8,4,10,4,12,4,208,9,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,5,5,219,8,5,10,5,12,5,222,9,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,236,8,6,10,6,12,6,239,9,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,248,8,7,1,8,1,8,1,8,1,8,1,8,3,
        8,255,8,8,1,9,1,9,1,9,1,9,1,9,3,9,262,8,9,1,9,1,9,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,3,11,274,8,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,286,8,11,1,12,1,12,1,12,3,12,291,8,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,300,8,13,1,14,1,14,1,
        15,1,15,1,15,1,15,1,15,1,15,3,15,310,8,15,1,16,1,16,1,17,1,17,1,
        18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,325,8,19,1,20,1,
        20,1,21,1,21,5,21,331,8,21,10,21,12,21,334,9,21,1,21,3,21,337,8,
        21,1,21,1,21,3,21,341,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,
        23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,361,8,
        24,10,24,12,24,364,9,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,411,
        8,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,419,8,30,1,30,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,1,31,1,32,4,32,431,8,32,11,32,12,32,432,
        1,32,4,32,436,8,32,11,32,12,32,437,3,32,440,8,32,1,33,1,33,3,33,
        444,8,33,1,33,1,33,5,33,448,8,33,10,33,12,33,451,9,33,1,33,1,33,
        3,33,455,8,33,1,33,3,33,458,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,36,3,36,478,
        8,36,1,36,5,36,481,8,36,10,36,12,36,484,9,36,1,36,1,36,3,36,488,
        8,36,1,36,3,36,491,8,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,38,
        1,38,1,38,3,38,503,8,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,
        3,39,513,8,39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,3,40,
        524,8,40,1,40,1,40,1,41,1,41,1,41,1,41,5,41,532,8,41,10,41,12,41,
        535,9,41,1,41,3,41,538,8,41,1,41,1,41,1,41,3,41,543,8,41,1,42,1,
        42,1,42,1,42,3,42,549,8,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,
        43,1,44,1,44,1,45,1,45,1,45,1,45,1,45,0,5,4,6,8,10,12,46,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,0,2,
        1,0,19,22,1,0,26,29,598,0,92,1,0,0,0,2,159,1,0,0,0,4,161,1,0,0,0,
        6,172,1,0,0,0,8,183,1,0,0,0,10,209,1,0,0,0,12,223,1,0,0,0,14,247,
        1,0,0,0,16,254,1,0,0,0,18,256,1,0,0,0,20,265,1,0,0,0,22,285,1,0,
        0,0,24,290,1,0,0,0,26,299,1,0,0,0,28,301,1,0,0,0,30,309,1,0,0,0,
        32,311,1,0,0,0,34,313,1,0,0,0,36,315,1,0,0,0,38,324,1,0,0,0,40,326,
        1,0,0,0,42,340,1,0,0,0,44,342,1,0,0,0,46,348,1,0,0,0,48,354,1,0,
        0,0,50,367,1,0,0,0,52,371,1,0,0,0,54,379,1,0,0,0,56,388,1,0,0,0,
        58,393,1,0,0,0,60,401,1,0,0,0,62,425,1,0,0,0,64,439,1,0,0,0,66,457,
        1,0,0,0,68,459,1,0,0,0,70,468,1,0,0,0,72,490,1,0,0,0,74,492,1,0,
        0,0,76,497,1,0,0,0,78,507,1,0,0,0,80,519,1,0,0,0,82,542,1,0,0,0,
        84,544,1,0,0,0,86,555,1,0,0,0,88,558,1,0,0,0,90,560,1,0,0,0,92,93,
        3,2,1,0,93,1,1,0,0,0,94,95,3,4,2,0,95,96,5,1,0,0,96,160,1,0,0,0,
        97,98,3,4,2,0,98,99,5,1,0,0,99,100,3,2,1,0,100,160,1,0,0,0,101,102,
        3,64,32,0,102,103,3,2,1,0,103,160,1,0,0,0,104,105,3,68,34,0,105,
        106,3,2,1,0,106,160,1,0,0,0,107,108,3,70,35,0,108,109,3,2,1,0,109,
        160,1,0,0,0,110,111,3,74,37,0,111,112,5,1,0,0,112,113,3,2,1,0,113,
        160,1,0,0,0,114,115,3,18,9,0,115,116,3,2,1,0,116,160,1,0,0,0,117,
        118,3,20,10,0,118,119,5,1,0,0,119,120,3,2,1,0,120,160,1,0,0,0,121,
        122,3,84,42,0,122,123,3,2,1,0,123,160,1,0,0,0,124,125,3,22,11,0,
        125,126,5,1,0,0,126,127,3,2,1,0,127,160,1,0,0,0,128,129,3,44,22,
        0,129,130,3,2,1,0,130,160,1,0,0,0,131,132,3,62,31,0,132,133,3,2,
        1,0,133,160,1,0,0,0,134,135,3,42,21,0,135,136,3,2,1,0,136,160,1,
        0,0,0,137,138,5,44,0,0,138,139,5,1,0,0,139,160,3,2,1,0,140,141,5,
        45,0,0,141,142,5,1,0,0,142,160,3,2,1,0,143,144,3,90,45,0,144,145,
        3,2,1,0,145,160,1,0,0,0,146,147,3,76,38,0,147,148,3,2,1,0,148,160,
        1,0,0,0,149,150,3,78,39,0,150,151,3,2,1,0,151,160,1,0,0,0,152,153,
        3,86,43,0,153,154,3,2,1,0,154,160,1,0,0,0,155,156,3,46,23,0,156,
        157,3,2,1,0,157,160,1,0,0,0,158,160,1,0,0,0,159,94,1,0,0,0,159,97,
        1,0,0,0,159,101,1,0,0,0,159,104,1,0,0,0,159,107,1,0,0,0,159,110,
        1,0,0,0,159,114,1,0,0,0,159,117,1,0,0,0,159,121,1,0,0,0,159,124,
        1,0,0,0,159,128,1,0,0,0,159,131,1,0,0,0,159,134,1,0,0,0,159,137,
        1,0,0,0,159,140,1,0,0,0,159,143,1,0,0,0,159,146,1,0,0,0,159,149,
        1,0,0,0,159,152,1,0,0,0,159,155,1,0,0,0,159,158,1,0,0,0,160,3,1,
        0,0,0,161,162,6,2,-1,0,162,163,3,6,3,0,163,169,1,0,0,0,164,165,10,
        2,0,0,165,166,5,2,0,0,166,168,3,6,3,0,167,164,1,0,0,0,168,171,1,
        0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,5,1,0,0,0,171,169,1,0,
        0,0,172,173,6,3,-1,0,173,174,3,8,4,0,174,180,1,0,0,0,175,176,10,
        2,0,0,176,177,5,3,0,0,177,179,3,8,4,0,178,175,1,0,0,0,179,182,1,
        0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,7,1,0,0,0,182,180,1,0,
        0,0,183,184,6,4,-1,0,184,185,3,10,5,0,185,206,1,0,0,0,186,187,10,
        7,0,0,187,188,5,4,0,0,188,205,3,10,5,0,189,190,10,6,0,0,190,191,
        5,5,0,0,191,205,3,10,5,0,192,193,10,5,0,0,193,194,5,6,0,0,194,205,
        3,10,5,0,195,196,10,4,0,0,196,197,5,7,0,0,197,205,3,10,5,0,198,199,
        10,3,0,0,199,200,5,8,0,0,200,205,3,10,5,0,201,202,10,2,0,0,202,203,
        5,9,0,0,203,205,3,10,5,0,204,186,1,0,0,0,204,189,1,0,0,0,204,192,
        1,0,0,0,204,195,1,0,0,0,204,198,1,0,0,0,204,201,1,0,0,0,205,208,
        1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,9,1,0,0,0,208,206,1,
        0,0,0,209,210,6,5,-1,0,210,211,3,12,6,0,211,220,1,0,0,0,212,213,
        10,3,0,0,213,214,5,10,0,0,214,219,3,12,6,0,215,216,10,2,0,0,216,
        217,5,11,0,0,217,219,3,12,6,0,218,212,1,0,0,0,218,215,1,0,0,0,219,
        222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,11,1,0,0,0,222,220,
        1,0,0,0,223,224,6,6,-1,0,224,225,3,14,7,0,225,237,1,0,0,0,226,227,
        10,4,0,0,227,228,5,42,0,0,228,236,3,14,7,0,229,230,10,3,0,0,230,
        231,5,12,0,0,231,236,3,14,7,0,232,233,10,2,0,0,233,234,5,13,0,0,
        234,236,3,14,7,0,235,226,1,0,0,0,235,229,1,0,0,0,235,232,1,0,0,0,
        236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,13,1,0,0,0,239,
        237,1,0,0,0,240,241,5,10,0,0,241,248,3,16,8,0,242,243,5,11,0,0,243,
        248,3,16,8,0,244,245,5,14,0,0,245,248,3,16,8,0,246,248,3,16,8,0,
        247,240,1,0,0,0,247,242,1,0,0,0,247,244,1,0,0,0,247,246,1,0,0,0,
        248,15,1,0,0,0,249,250,5,15,0,0,250,251,3,4,2,0,251,252,5,16,0,0,
        252,255,1,0,0,0,253,255,3,30,15,0,254,249,1,0,0,0,254,253,1,0,0,
        0,255,17,1,0,0,0,256,257,3,20,10,0,257,261,5,17,0,0,258,262,3,4,
        2,0,259,262,3,74,37,0,260,262,3,80,40,0,261,258,1,0,0,0,261,259,
        1,0,0,0,261,260,1,0,0,0,262,263,1,0,0,0,263,264,5,1,0,0,264,19,1,
        0,0,0,265,266,3,24,12,0,266,267,3,38,19,0,267,21,1,0,0,0,268,269,
        3,38,19,0,269,273,5,17,0,0,270,274,3,10,5,0,271,274,3,74,37,0,272,
        274,3,80,40,0,273,270,1,0,0,0,273,271,1,0,0,0,273,272,1,0,0,0,274,
        286,1,0,0,0,275,276,3,30,15,0,276,277,5,17,0,0,277,278,3,10,5,0,
        278,286,1,0,0,0,279,280,5,15,0,0,280,281,3,4,2,0,281,282,5,16,0,
        0,282,283,5,17,0,0,283,284,3,4,2,0,284,286,1,0,0,0,285,268,1,0,0,
        0,285,275,1,0,0,0,285,279,1,0,0,0,286,23,1,0,0,0,287,288,5,18,0,
        0,288,291,3,26,13,0,289,291,3,26,13,0,290,287,1,0,0,0,290,289,1,
        0,0,0,291,25,1,0,0,0,292,293,3,28,14,0,293,294,5,42,0,0,294,300,
        1,0,0,0,295,296,3,28,14,0,296,297,5,43,0,0,297,300,1,0,0,0,298,300,
        3,28,14,0,299,292,1,0,0,0,299,295,1,0,0,0,299,298,1,0,0,0,300,27,
        1,0,0,0,301,302,7,0,0,0,302,29,1,0,0,0,303,310,3,32,16,0,304,310,
        3,34,17,0,305,310,3,36,18,0,306,310,3,38,19,0,307,310,3,74,37,0,
        308,310,3,80,40,0,309,303,1,0,0,0,309,304,1,0,0,0,309,305,1,0,0,
        0,309,306,1,0,0,0,309,307,1,0,0,0,309,308,1,0,0,0,310,31,1,0,0,0,
        311,312,5,48,0,0,312,33,1,0,0,0,313,314,5,49,0,0,314,35,1,0,0,0,
        315,316,5,47,0,0,316,37,1,0,0,0,317,318,5,23,0,0,318,325,3,40,20,
        0,319,320,5,42,0,0,320,325,3,40,20,0,321,322,5,43,0,0,322,325,3,
        40,20,0,323,325,3,40,20,0,324,317,1,0,0,0,324,319,1,0,0,0,324,321,
        1,0,0,0,324,323,1,0,0,0,325,39,1,0,0,0,326,327,5,46,0,0,327,41,1,
        0,0,0,328,332,3,52,26,0,329,331,3,54,27,0,330,329,1,0,0,0,331,334,
        1,0,0,0,332,330,1,0,0,0,332,333,1,0,0,0,333,336,1,0,0,0,334,332,
        1,0,0,0,335,337,3,56,28,0,336,335,1,0,0,0,336,337,1,0,0,0,337,341,
        1,0,0,0,338,341,3,58,29,0,339,341,3,60,30,0,340,328,1,0,0,0,340,
        338,1,0,0,0,340,339,1,0,0,0,341,43,1,0,0,0,342,343,5,24,0,0,343,
        344,5,15,0,0,344,345,3,50,25,0,345,346,5,16,0,0,346,347,5,1,0,0,
        347,45,1,0,0,0,348,349,5,25,0,0,349,350,5,15,0,0,350,351,3,48,24,
        0,351,352,5,16,0,0,352,353,5,1,0,0,353,47,1,0,0,0,354,355,7,1,0,
        0,355,356,5,30,0,0,356,362,1,0,0,0,357,358,3,40,20,0,358,359,5,30,
        0,0,359,361,1,0,0,0,360,357,1,0,0,0,361,364,1,0,0,0,362,360,1,0,
        0,0,362,363,1,0,0,0,363,365,1,0,0,0,364,362,1,0,0,0,365,366,3,40,
        20,0,366,49,1,0,0,0,367,368,7,1,0,0,368,369,5,30,0,0,369,370,3,30,
        15,0,370,51,1,0,0,0,371,372,5,31,0,0,372,373,5,15,0,0,373,374,3,
        4,2,0,374,375,5,16,0,0,375,376,5,32,0,0,376,377,3,88,44,0,377,378,
        5,33,0,0,378,53,1,0,0,0,379,380,5,34,0,0,380,381,5,31,0,0,381,382,
        5,15,0,0,382,383,3,4,2,0,383,384,5,16,0,0,384,385,5,32,0,0,385,386,
        3,88,44,0,386,387,5,33,0,0,387,55,1,0,0,0,388,389,5,34,0,0,389,390,
        5,32,0,0,390,391,3,88,44,0,391,392,5,33,0,0,392,57,1,0,0,0,393,394,
        5,35,0,0,394,395,5,15,0,0,395,396,3,4,2,0,396,397,5,16,0,0,397,398,
        5,32,0,0,398,399,3,88,44,0,399,400,5,33,0,0,400,59,1,0,0,0,401,402,
        5,36,0,0,402,418,5,15,0,0,403,404,3,20,10,0,404,405,5,1,0,0,405,
        411,1,0,0,0,406,411,3,18,9,0,407,408,3,22,11,0,408,409,5,1,0,0,409,
        411,1,0,0,0,410,403,1,0,0,0,410,406,1,0,0,0,410,407,1,0,0,0,411,
        412,1,0,0,0,412,413,3,4,2,0,413,414,5,1,0,0,414,415,3,22,11,0,415,
        419,1,0,0,0,416,417,5,1,0,0,417,419,5,1,0,0,418,410,1,0,0,0,418,
        416,1,0,0,0,419,420,1,0,0,0,420,421,5,16,0,0,421,422,5,32,0,0,422,
        423,3,88,44,0,423,424,5,33,0,0,424,61,1,0,0,0,425,426,5,32,0,0,426,
        427,3,88,44,0,427,428,5,33,0,0,428,63,1,0,0,0,429,431,5,51,0,0,430,
        429,1,0,0,0,431,432,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,433,
        440,1,0,0,0,434,436,5,50,0,0,435,434,1,0,0,0,436,437,1,0,0,0,437,
        435,1,0,0,0,437,438,1,0,0,0,438,440,1,0,0,0,439,430,1,0,0,0,439,
        435,1,0,0,0,440,65,1,0,0,0,441,443,3,24,12,0,442,444,5,46,0,0,443,
        442,1,0,0,0,443,444,1,0,0,0,444,445,1,0,0,0,445,446,5,30,0,0,446,
        448,1,0,0,0,447,441,1,0,0,0,448,451,1,0,0,0,449,447,1,0,0,0,449,
        450,1,0,0,0,450,452,1,0,0,0,451,449,1,0,0,0,452,454,3,24,12,0,453,
        455,5,46,0,0,454,453,1,0,0,0,454,455,1,0,0,0,455,458,1,0,0,0,456,
        458,1,0,0,0,457,449,1,0,0,0,457,456,1,0,0,0,458,67,1,0,0,0,459,460,
        3,24,12,0,460,461,5,46,0,0,461,462,5,15,0,0,462,463,3,66,33,0,463,
        464,5,16,0,0,464,465,5,32,0,0,465,466,3,88,44,0,466,467,5,33,0,0,
        467,69,1,0,0,0,468,469,3,24,12,0,469,470,5,46,0,0,470,471,5,15,0,
        0,471,472,3,66,33,0,472,473,5,16,0,0,473,474,5,1,0,0,474,71,1,0,
        0,0,475,478,5,46,0,0,476,478,3,30,15,0,477,475,1,0,0,0,477,476,1,
        0,0,0,478,479,1,0,0,0,479,481,5,30,0,0,480,477,1,0,0,0,481,484,1,
        0,0,0,482,480,1,0,0,0,482,483,1,0,0,0,483,487,1,0,0,0,484,482,1,
        0,0,0,485,488,5,46,0,0,486,488,3,30,15,0,487,485,1,0,0,0,487,486,
        1,0,0,0,488,491,1,0,0,0,489,491,1,0,0,0,490,482,1,0,0,0,490,489,
        1,0,0,0,491,73,1,0,0,0,492,493,5,46,0,0,493,494,5,15,0,0,494,495,
        3,72,36,0,495,496,5,16,0,0,496,75,1,0,0,0,497,498,3,24,12,0,498,
        499,5,46,0,0,499,502,5,37,0,0,500,503,5,48,0,0,501,503,3,40,20,0,
        502,500,1,0,0,0,502,501,1,0,0,0,503,504,1,0,0,0,504,505,5,38,0,0,
        505,506,5,1,0,0,506,77,1,0,0,0,507,508,3,24,12,0,508,509,5,46,0,
        0,509,512,5,37,0,0,510,513,5,48,0,0,511,513,3,40,20,0,512,510,1,
        0,0,0,512,511,1,0,0,0,513,514,1,0,0,0,514,515,5,38,0,0,515,516,5,
        17,0,0,516,517,3,82,41,0,517,518,5,1,0,0,518,79,1,0,0,0,519,520,
        3,40,20,0,520,523,5,37,0,0,521,524,5,48,0,0,522,524,3,40,20,0,523,
        521,1,0,0,0,523,522,1,0,0,0,524,525,1,0,0,0,525,526,5,38,0,0,526,
        81,1,0,0,0,527,533,5,32,0,0,528,529,3,30,15,0,529,530,5,30,0,0,530,
        532,1,0,0,0,531,528,1,0,0,0,532,535,1,0,0,0,533,531,1,0,0,0,533,
        534,1,0,0,0,534,537,1,0,0,0,535,533,1,0,0,0,536,538,3,30,15,0,537,
        536,1,0,0,0,537,538,1,0,0,0,538,539,1,0,0,0,539,543,5,33,0,0,540,
        541,5,32,0,0,541,543,5,33,0,0,542,527,1,0,0,0,542,540,1,0,0,0,543,
        83,1,0,0,0,544,545,5,46,0,0,545,548,5,37,0,0,546,549,5,48,0,0,547,
        549,3,40,20,0,548,546,1,0,0,0,548,547,1,0,0,0,549,550,1,0,0,0,550,
        551,5,38,0,0,551,552,5,17,0,0,552,553,3,30,15,0,553,554,5,1,0,0,
        554,85,1,0,0,0,555,556,5,39,0,0,556,557,5,40,0,0,557,87,1,0,0,0,
        558,559,3,2,1,0,559,89,1,0,0,0,560,561,5,41,0,0,561,562,3,4,2,0,
        562,563,5,1,0,0,563,91,1,0,0,0,42,159,169,180,204,206,218,220,235,
        237,247,254,261,273,285,290,299,309,324,332,336,340,362,410,418,
        432,437,439,443,449,454,457,477,482,487,490,502,512,523,533,537,
        542,548
    ]

class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'&&'", "'||'", "'=='", "'<='", 
                     "'>='", "'!='", "'<'", "'>'", "'+'", "'-'", "'/'", 
                     "'%'", "'!'", "'('", "')'", "'='", "'const'", "'int'", 
                     "'float'", "'char'", "'void'", "'&'", "'printf'", "'scanf'", 
                     "'\"%d\"'", "'\"%i\"'", "'\"%s\"'", "'\"%c\"'", "','", 
                     "'if'", "'{'", "'}'", "'else'", "'while'", "'for'", 
                     "'['", "']'", "'#include'", "'<stdio.h>'", "'return'", 
                     "'*'", "<INVALID>", "'break'", "'continue'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "POINTER", "POINTERS", "BREAK", 
                      "CONTINUE", "ID", "CHAR", "INT", "FLOAT", "COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

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
    RULE_conditionStatement = 21
    RULE_printFunction = 22
    RULE_scanFunction = 23
    RULE_scanArg = 24
    RULE_printArg = 25
    RULE_ifStatement = 26
    RULE_elifStatement = 27
    RULE_elseStatement = 28
    RULE_whileStatement = 29
    RULE_forLoop = 30
    RULE_unNamedScope = 31
    RULE_comment = 32
    RULE_argument = 33
    RULE_funcDefinition = 34
    RULE_funcDeclaration = 35
    RULE_argumentCall = 36
    RULE_functionCall = 37
    RULE_arrDecl = 38
    RULE_arrDef = 39
    RULE_arrCall = 40
    RULE_arrArg = 41
    RULE_arrAssign = 42
    RULE_lib = 43
    RULE_body = 44
    RULE_returnStatement = 45

    ruleNames =  [ "prog", "expr", "opAnd", "opOr", "opCompare", "opAddOrSub", 
                   "opMultOrDiv", "opUnary", "brackets", "variableDefinition", 
                   "variableDeclaration", "assignmentStatement", "constWord", 
                   "pointerWord", "reservedWord", "dataTypes", "int", "float", 
                   "char", "referenceID", "nameIdentifier", "conditionStatement", 
                   "printFunction", "scanFunction", "scanArg", "printArg", 
                   "ifStatement", "elifStatement", "elseStatement", "whileStatement", 
                   "forLoop", "unNamedScope", "comment", "argument", "funcDefinition", 
                   "funcDeclaration", "argumentCall", "functionCall", "arrDecl", 
                   "arrDef", "arrCall", "arrArg", "arrAssign", "lib", "body", 
                   "returnStatement" ]

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
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    POINTER=42
    POINTERS=43
    BREAK=44
    CONTINUE=45
    ID=46
    CHAR=47
    INT=48
    FLOAT=49
    COMMENT=50
    BLOCK_COMMENT=51
    WS=52

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
            self.state = 92
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


        def arrAssign(self):
            return self.getTypedRuleContext(MyGrammarParser.ArrAssignContext,0)


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


        def arrDecl(self):
            return self.getTypedRuleContext(MyGrammarParser.ArrDeclContext,0)


        def arrDef(self):
            return self.getTypedRuleContext(MyGrammarParser.ArrDefContext,0)


        def lib(self):
            return self.getTypedRuleContext(MyGrammarParser.LibContext,0)


        def scanFunction(self):
            return self.getTypedRuleContext(MyGrammarParser.ScanFunctionContext,0)


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
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.opAnd(0)
                self.state = 95
                self.match(MyGrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.opAnd(0)
                self.state = 98
                self.match(MyGrammarParser.T__0)
                self.state = 99
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.comment()
                self.state = 102
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.funcDefinition()
                self.state = 105
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.funcDeclaration()
                self.state = 108
                self.expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 110
                self.functionCall()
                self.state = 111
                self.match(MyGrammarParser.T__0)
                self.state = 112
                self.expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.variableDefinition()
                self.state = 115
                self.expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 117
                self.variableDeclaration()
                self.state = 118
                self.match(MyGrammarParser.T__0)
                self.state = 119
                self.expr()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 121
                self.arrAssign()
                self.state = 122
                self.expr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 124
                self.assignmentStatement()
                self.state = 125
                self.match(MyGrammarParser.T__0)
                self.state = 126
                self.expr()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 128
                self.printFunction()
                self.state = 129
                self.expr()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 131
                self.unNamedScope()
                self.state = 132
                self.expr()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 134
                self.conditionStatement()
                self.state = 135
                self.expr()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 137
                self.match(MyGrammarParser.BREAK)
                self.state = 138
                self.match(MyGrammarParser.T__0)
                self.state = 139
                self.expr()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 140
                self.match(MyGrammarParser.CONTINUE)
                self.state = 141
                self.match(MyGrammarParser.T__0)
                self.state = 142
                self.expr()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 143
                self.returnStatement()
                self.state = 144
                self.expr()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 146
                self.arrDecl()
                self.state = 147
                self.expr()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 149
                self.arrDef()
                self.state = 150
                self.expr()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 152
                self.lib()
                self.state = 153
                self.expr()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 155
                self.scanFunction()
                self.state = 156
                self.expr()
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)

                pass


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
            self.state = 162
            self.opOr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpAndContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opAnd)
                    self.state = 164
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 165
                    self.match(MyGrammarParser.T__1)
                    self.state = 166
                    self.opOr(0) 
                self.state = 171
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
            self.state = 173
            self.opCompare(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammarParser.OpOrContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_opOr)
                    self.state = 175
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 176
                    self.match(MyGrammarParser.T__2)
                    self.state = 177
                    self.opCompare(0) 
                self.state = 182
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
            self.state = 184
            self.opAddOrSub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 204
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 186
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 187
                        self.match(MyGrammarParser.T__3)
                        self.state = 188
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 189
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 190
                        self.match(MyGrammarParser.T__4)
                        self.state = 191
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 192
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 193
                        self.match(MyGrammarParser.T__5)
                        self.state = 194
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 195
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 196
                        self.match(MyGrammarParser.T__6)
                        self.state = 197
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 5:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 198
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 199
                        self.match(MyGrammarParser.T__7)
                        self.state = 200
                        self.opAddOrSub(0)
                        pass

                    elif la_ == 6:
                        localctx = MyGrammarParser.OpCompareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opCompare)
                        self.state = 201
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 202
                        self.match(MyGrammarParser.T__8)
                        self.state = 203
                        self.opAddOrSub(0)
                        pass

             
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
            self.state = 210
            self.opMultOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 218
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 212
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 213
                        self.match(MyGrammarParser.T__9)
                        self.state = 214
                        self.opMultOrDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpAddOrSubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opAddOrSub)
                        self.state = 215
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 216
                        self.match(MyGrammarParser.T__10)
                        self.state = 217
                        self.opMultOrDiv(0)
                        pass

             
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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


        def POINTER(self):
            return self.getToken(MyGrammarParser.POINTER, 0)

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
            self.state = 224
            self.opUnary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 235
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 226
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 227
                        self.match(MyGrammarParser.POINTER)
                        self.state = 228
                        self.opUnary()
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 229
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 230
                        self.match(MyGrammarParser.T__11)
                        self.state = 231
                        self.opUnary()
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.OpMultOrDivContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_opMultOrDiv)
                        self.state = 232
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 233
                        self.match(MyGrammarParser.T__12)
                        self.state = 234
                        self.opUnary()
                        pass

             
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(MyGrammarParser.T__9)
                self.state = 241
                self.brackets()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(MyGrammarParser.T__10)
                self.state = 243
                self.brackets()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.match(MyGrammarParser.T__13)
                self.state = 245
                self.brackets()
                pass
            elif token in [15, 23, 42, 43, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
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
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.match(MyGrammarParser.T__14)
                self.state = 250
                self.opAnd(0)
                self.state = 251
                self.match(MyGrammarParser.T__15)
                pass
            elif token in [23, 42, 43, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.dataTypes()
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


    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(MyGrammarParser.VariableDeclarationContext,0)


        def opAnd(self):
            return self.getTypedRuleContext(MyGrammarParser.OpAndContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MyGrammarParser.FunctionCallContext,0)


        def arrCall(self):
            return self.getTypedRuleContext(MyGrammarParser.ArrCallContext,0)


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
            self.state = 256
            self.variableDeclaration()
            self.state = 257
            self.match(MyGrammarParser.T__16)
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 258
                self.opAnd(0)
                pass

            elif la_ == 2:
                self.state = 259
                self.functionCall()
                pass

            elif la_ == 3:
                self.state = 260
                self.arrCall()
                pass


            self.state = 263
            self.match(MyGrammarParser.T__0)
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
            self.state = 265
            self.constWord()
            self.state = 266
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


        def functionCall(self):
            return self.getTypedRuleContext(MyGrammarParser.FunctionCallContext,0)


        def arrCall(self):
            return self.getTypedRuleContext(MyGrammarParser.ArrCallContext,0)


        def dataTypes(self):
            return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,0)


        def opAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.OpAndContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.OpAndContext,i)


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
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.referenceID()
                self.state = 269
                self.match(MyGrammarParser.T__16)
                self.state = 273
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 270
                    self.opAddOrSub(0)
                    pass

                elif la_ == 2:
                    self.state = 271
                    self.functionCall()
                    pass

                elif la_ == 3:
                    self.state = 272
                    self.arrCall()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.dataTypes()
                self.state = 276
                self.match(MyGrammarParser.T__16)
                self.state = 277
                self.opAddOrSub(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.match(MyGrammarParser.T__14)
                self.state = 280
                self.opAnd(0)
                self.state = 281
                self.match(MyGrammarParser.T__15)
                self.state = 282
                self.match(MyGrammarParser.T__16)
                self.state = 283
                self.opAnd(0)
                pass


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
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(MyGrammarParser.T__17)
                self.state = 288
                self.pointerWord()
                pass
            elif token in [19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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


        def POINTER(self):
            return self.getToken(MyGrammarParser.POINTER, 0)

        def POINTERS(self):
            return self.getToken(MyGrammarParser.POINTERS, 0)

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
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.reservedWord()
                self.state = 293
                self.match(MyGrammarParser.POINTER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.reservedWord()
                self.state = 296
                self.match(MyGrammarParser.POINTERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
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
            self.state = 301
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
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


        def functionCall(self):
            return self.getTypedRuleContext(MyGrammarParser.FunctionCallContext,0)


        def arrCall(self):
            return self.getTypedRuleContext(MyGrammarParser.ArrCallContext,0)


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
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.int_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.float_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.char()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 306
                self.referenceID()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 307
                self.functionCall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 308
                self.arrCall()
                pass


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
            self.state = 311
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
            self.state = 313
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
            self.state = 315
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


        def POINTER(self):
            return self.getToken(MyGrammarParser.POINTER, 0)

        def POINTERS(self):
            return self.getToken(MyGrammarParser.POINTERS, 0)

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
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(MyGrammarParser.T__22)
                self.state = 318
                self.nameIdentifier()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(MyGrammarParser.POINTER)
                self.state = 320
                self.nameIdentifier()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 321
                self.match(MyGrammarParser.POINTERS)
                self.state = 322
                self.nameIdentifier()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
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
            self.state = 326
            self.match(MyGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.IfStatementContext,0)


        def elifStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ElifStatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ElifStatementContext,i)


        def elseStatement(self):
            return self.getTypedRuleContext(MyGrammarParser.ElseStatementContext,0)


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
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.ifStatement()
                self.state = 332
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 329
                        self.elifStatement() 
                    self.state = 334
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 335
                    self.elseStatement()


                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.whileStatement()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
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

        def printArg(self):
            return self.getTypedRuleContext(MyGrammarParser.PrintArgContext,0)


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
            self.state = 342
            self.match(MyGrammarParser.T__23)
            self.state = 343
            self.match(MyGrammarParser.T__14)
            self.state = 344
            self.printArg()
            self.state = 345
            self.match(MyGrammarParser.T__15)
            self.state = 346
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scanArg(self):
            return self.getTypedRuleContext(MyGrammarParser.ScanArgContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_scanFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanFunction" ):
                listener.enterScanFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanFunction" ):
                listener.exitScanFunction(self)




    def scanFunction(self):

        localctx = MyGrammarParser.ScanFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_scanFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MyGrammarParser.T__24)
            self.state = 349
            self.match(MyGrammarParser.T__14)
            self.state = 350
            self.scanArg()
            self.state = 351
            self.match(MyGrammarParser.T__15)
            self.state = 352
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.NameIdentifierContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.NameIdentifierContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_scanArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanArg" ):
                listener.enterScanArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanArg" ):
                listener.exitScanArg(self)




    def scanArg(self):

        localctx = MyGrammarParser.ScanArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_scanArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 355
            self.match(MyGrammarParser.T__29)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 357
                    self.nameIdentifier()
                    self.state = 358
                    self.match(MyGrammarParser.T__29) 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 365
            self.nameIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataTypes(self):
            return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_printArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintArg" ):
                listener.enterPrintArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintArg" ):
                listener.exitPrintArg(self)




    def printArg(self):

        localctx = MyGrammarParser.PrintArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_printArg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 368
            self.match(MyGrammarParser.T__29)
            self.state = 369
            self.dataTypes()
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
        self.enterRule(localctx, 52, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(MyGrammarParser.T__30)
            self.state = 372
            self.match(MyGrammarParser.T__14)
            self.state = 373
            self.opAnd(0)
            self.state = 374
            self.match(MyGrammarParser.T__15)
            self.state = 375
            self.match(MyGrammarParser.T__31)
            self.state = 376
            self.body()
            self.state = 377
            self.match(MyGrammarParser.T__32)
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
        self.enterRule(localctx, 54, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(MyGrammarParser.T__33)
            self.state = 380
            self.match(MyGrammarParser.T__30)
            self.state = 381
            self.match(MyGrammarParser.T__14)
            self.state = 382
            self.opAnd(0)
            self.state = 383
            self.match(MyGrammarParser.T__15)
            self.state = 384
            self.match(MyGrammarParser.T__31)
            self.state = 385
            self.body()
            self.state = 386
            self.match(MyGrammarParser.T__32)
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
        self.enterRule(localctx, 56, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(MyGrammarParser.T__33)
            self.state = 389
            self.match(MyGrammarParser.T__31)
            self.state = 390
            self.body()
            self.state = 391
            self.match(MyGrammarParser.T__32)
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
        self.enterRule(localctx, 58, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MyGrammarParser.T__34)
            self.state = 394
            self.match(MyGrammarParser.T__14)
            self.state = 395
            self.opAnd(0)
            self.state = 396
            self.match(MyGrammarParser.T__15)
            self.state = 397
            self.match(MyGrammarParser.T__31)
            self.state = 398
            self.body()
            self.state = 399
            self.match(MyGrammarParser.T__32)
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
        self.enterRule(localctx, 60, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MyGrammarParser.T__35)
            self.state = 402
            self.match(MyGrammarParser.T__14)
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 18, 19, 20, 21, 22, 23, 42, 43, 46, 47, 48, 49]:
                self.state = 410
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 403
                    self.variableDeclaration()
                    self.state = 404
                    self.match(MyGrammarParser.T__0)
                    pass

                elif la_ == 2:
                    self.state = 406
                    self.variableDefinition()
                    pass

                elif la_ == 3:
                    self.state = 407
                    self.assignmentStatement()
                    self.state = 408
                    self.match(MyGrammarParser.T__0)
                    pass


                self.state = 412
                self.opAnd(0)
                self.state = 413
                self.match(MyGrammarParser.T__0)
                self.state = 414
                self.assignmentStatement()
                pass
            elif token in [1]:
                self.state = 416
                self.match(MyGrammarParser.T__0)
                self.state = 417
                self.match(MyGrammarParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 420
            self.match(MyGrammarParser.T__15)
            self.state = 421
            self.match(MyGrammarParser.T__31)
            self.state = 422
            self.body()
            self.state = 423
            self.match(MyGrammarParser.T__32)
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
        self.enterRule(localctx, 62, self.RULE_unNamedScope)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(MyGrammarParser.T__31)
            self.state = 426
            self.body()
            self.state = 427
            self.match(MyGrammarParser.T__32)
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
        self.enterRule(localctx, 64, self.RULE_comment)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 429
                        self.match(MyGrammarParser.BLOCK_COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 432 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 434
                        self.match(MyGrammarParser.COMMENT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 437 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 441
                        self.constWord()
                        self.state = 443
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==46:
                            self.state = 442
                            self.match(MyGrammarParser.ID)


                        self.state = 445
                        self.match(MyGrammarParser.T__29) 
                    self.state = 451
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                self.state = 452
                self.constWord()
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 453
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
        self.enterRule(localctx, 68, self.RULE_funcDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.constWord()
            self.state = 460
            self.match(MyGrammarParser.ID)
            self.state = 461
            self.match(MyGrammarParser.T__14)
            self.state = 462
            self.argument()
            self.state = 463
            self.match(MyGrammarParser.T__15)
            self.state = 464
            self.match(MyGrammarParser.T__31)
            self.state = 465
            self.body()
            self.state = 466
            self.match(MyGrammarParser.T__32)
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
        self.enterRule(localctx, 70, self.RULE_funcDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.constWord()
            self.state = 469
            self.match(MyGrammarParser.ID)
            self.state = 470
            self.match(MyGrammarParser.T__14)
            self.state = 471
            self.argument()
            self.state = 472
            self.match(MyGrammarParser.T__15)
            self.state = 473
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
        self.enterRule(localctx, 72, self.RULE_argumentCall)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 42, 43, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 477
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                        if la_ == 1:
                            self.state = 475
                            self.match(MyGrammarParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 476
                            self.dataTypes()
                            pass


                        self.state = 479
                        self.match(MyGrammarParser.T__29) 
                    self.state = 484
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 487
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 485
                    self.match(MyGrammarParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 486
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
        self.enterRule(localctx, 74, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(MyGrammarParser.ID)
            self.state = 493
            self.match(MyGrammarParser.T__14)
            self.state = 494
            self.argumentCall()
            self.state = 495
            self.match(MyGrammarParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ConstWordContext,0)


        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def nameIdentifier(self):
            return self.getTypedRuleContext(MyGrammarParser.NameIdentifierContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_arrDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrDecl" ):
                listener.enterArrDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrDecl" ):
                listener.exitArrDecl(self)




    def arrDecl(self):

        localctx = MyGrammarParser.ArrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arrDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.constWord()
            self.state = 498
            self.match(MyGrammarParser.ID)
            self.state = 499
            self.match(MyGrammarParser.T__36)
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 500
                self.match(MyGrammarParser.INT)
                pass
            elif token in [46]:
                self.state = 501
                self.nameIdentifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 504
            self.match(MyGrammarParser.T__37)
            self.state = 505
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constWord(self):
            return self.getTypedRuleContext(MyGrammarParser.ConstWordContext,0)


        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def arrArg(self):
            return self.getTypedRuleContext(MyGrammarParser.ArrArgContext,0)


        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def nameIdentifier(self):
            return self.getTypedRuleContext(MyGrammarParser.NameIdentifierContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_arrDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrDef" ):
                listener.enterArrDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrDef" ):
                listener.exitArrDef(self)




    def arrDef(self):

        localctx = MyGrammarParser.ArrDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_arrDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.constWord()
            self.state = 508
            self.match(MyGrammarParser.ID)
            self.state = 509
            self.match(MyGrammarParser.T__36)
            self.state = 512
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 510
                self.match(MyGrammarParser.INT)
                pass
            elif token in [46]:
                self.state = 511
                self.nameIdentifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 514
            self.match(MyGrammarParser.T__37)
            self.state = 515
            self.match(MyGrammarParser.T__16)
            self.state = 516
            self.arrArg()
            self.state = 517
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.NameIdentifierContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.NameIdentifierContext,i)


        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def getRuleIndex(self):
            return MyGrammarParser.RULE_arrCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrCall" ):
                listener.enterArrCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrCall" ):
                listener.exitArrCall(self)




    def arrCall(self):

        localctx = MyGrammarParser.ArrCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arrCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.nameIdentifier()
            self.state = 520
            self.match(MyGrammarParser.T__36)
            self.state = 523
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 521
                self.match(MyGrammarParser.INT)
                pass
            elif token in [46]:
                self.state = 522
                self.nameIdentifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 525
            self.match(MyGrammarParser.T__37)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataTypes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.DataTypesContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_arrArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrArg" ):
                listener.enterArrArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrArg" ):
                listener.exitArrArg(self)




    def arrArg(self):

        localctx = MyGrammarParser.ArrArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arrArg)
        self._la = 0 # Token type
        try:
            self.state = 542
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.match(MyGrammarParser.T__31)
                self.state = 533
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 528
                        self.dataTypes()
                        self.state = 529
                        self.match(MyGrammarParser.T__29) 
                    self.state = 535
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 537
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1068725310586880) != 0):
                    self.state = 536
                    self.dataTypes()


                self.state = 539
                self.match(MyGrammarParser.T__32)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.match(MyGrammarParser.T__31)
                self.state = 541
                self.match(MyGrammarParser.T__32)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyGrammarParser.ID, 0)

        def dataTypes(self):
            return self.getTypedRuleContext(MyGrammarParser.DataTypesContext,0)


        def INT(self):
            return self.getToken(MyGrammarParser.INT, 0)

        def nameIdentifier(self):
            return self.getTypedRuleContext(MyGrammarParser.NameIdentifierContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_arrAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrAssign" ):
                listener.enterArrAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrAssign" ):
                listener.exitArrAssign(self)




    def arrAssign(self):

        localctx = MyGrammarParser.ArrAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arrAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(MyGrammarParser.ID)
            self.state = 545
            self.match(MyGrammarParser.T__36)
            self.state = 548
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.state = 546
                self.match(MyGrammarParser.INT)
                pass
            elif token in [46]:
                self.state = 547
                self.nameIdentifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 550
            self.match(MyGrammarParser.T__37)
            self.state = 551
            self.match(MyGrammarParser.T__16)
            self.state = 552
            self.dataTypes()
            self.state = 553
            self.match(MyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LibContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_lib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLib" ):
                listener.enterLib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLib" ):
                listener.exitLib(self)




    def lib(self):

        localctx = MyGrammarParser.LibContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_lib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.match(MyGrammarParser.T__38)
            self.state = 556
            self.match(MyGrammarParser.T__39)
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
        self.enterRule(localctx, 88, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
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
        self.enterRule(localctx, 90, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(MyGrammarParser.T__40)
            self.state = 561
            self.opAnd(0)
            self.state = 562
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
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

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
         




