import math
import sys
from File_Loader import *
from PrettyPrint import *
from LinearLearner import *
from Validation import *

eta = .000001
iterations = 80000

E = file_loader("chocodata.txt")
V = file_loader("chocovalid.txt")
w = Linear_Learner(E, eta, iterations)
error = validation(V, w)
pretty_print(w, eta, iterations, error)