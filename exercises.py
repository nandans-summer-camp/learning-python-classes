###########################################
# PART A: Patient
###########################################


def _covid_prob(symptoms):
    covid_list = ['cough', 'fever', 'anosmia']
    prob = 0.05
    for s in symptoms:
        if s in covid_list:
            prob += 0.10
    return prob

class Patient():
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name, res):
        self.tests[test_name] = res

    def has_covid(self):
        try:
            if self.tests['covid']:
                return 0.99
            return 0.01
        except KeyError:
            return _covid_prob(self.symptoms)

#
# In this exercise we will make an "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively


#
# 2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.



#
# 3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']




###########################################
# PART B: Encoder
###########################################


class Encoder():
    def __init__(self):
        self.idx = 0
        self.lookup = {}

    def fit(self, items):
        for item in items:
            try:
                self.lookup[item]
            except KeyError:
                self.lookup[item] = self.idx
                self.idx += 1
            except TypeError:
                raise Exception('Encoder.encode() was passed elements that it cannot encode')

    def export_mapping(self):
        return self.lookup

    def import_mapping(self, mapping):
        self.lookup = mapping

    def encode(self, items):
        self.fit(items)
        return [self.lookup[i] for i in items]

    def decode(self, coded):
        reverse = {v:k for k, v in self.lookup.items()}
        try:
            return [reverse[c] for c in coded]
        except KeyError:
            raise Exception('Encoder.decode() was passed integers that it cannot decode')

#
# In this exercise we will make an "Encoder" class
#
# The Encoder class should be able to encode
# a list of strings into a list of
# integers that can later be losslessly
# decoded.
#
# For example, if given a list of words:
# ['Joan', 'went', 'to', 'the', 'store']
# it might encode:
# [245, 9873, 290, 10, 209]
# and be able to decode it back again
# to the list of words.
#
#
#
# 4)
# Create a class called "Encoder."
# The constructor should have no
# parameters (besides, of course, "self")
#
#
#
# 5)
# Add two methods: "encode" and "decode"

# "encode" should have a single parameter,
# a list of strings, and returns
# a list of integers which represents the
# encoding.
#
# "decode" should have a single parameter,
# a list of integers, and returns a list
# of strings, which should be the same as
# was passed to "encode"


##################################
# BONUS EXERCISES
##################################


# 6)
# Your encoder has learned a "mapping"
# from strings to ints in order to encode
# its input data.
#
# Imagine we want to be able to "export"
# that mapping from one encoder and load it
# into another.
#
# Create a method called "export_mapping"
# and a method called "import_mapping".
#
# "export_mapping" should have no parameters,
# and should return an object that can be
# imported into another Encoder instance
# via the "import_mapping" method and
# used to encode/decode in the same way
# as the original.
#
#
#
# 7)
# Modify your method "encode" so that it
# raises an exception if the input list
# has elements that cannot be encoded.
# (for example, if instead of a string,
# the list contains a nested complex data
# type, like a list or dictionary)
#
# The exception should say:
# "Encoder.encode() was passed elements that it cannot encode"
#
#
#
# 8)
# Modify your method "decode" so that it
# raises a helpful exception if it cannot decode
# an integer in the provided list.
#
# The exception should say:
# "Encoder.decode() was passed integers that it cannot decode"
