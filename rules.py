import math
from entry_fuzzyfication import fuzzyfy_value

def find_params_0_order():
    learning_rate = 0.0005
    iterations = 2000
    params = [0,0,0]
    x = [i * 0.05 for i in range(0, int(7 / 0.05) + 1)]

    for _ in range(iterations):

            for value in x:
                real_value = math.sin(value)
                activations = fuzzyfy_value(value)
                num = 0
                den = 0

                for index2,pertinency in enumerate(activations):
                    num += pertinency*params[index2]*value
                    den += pertinency

                estimated_value = num/den
                error = estimated_value - real_value
                
                for index in range(len(params)):
                    params[index] -= learning_rate * value * activations[index] * error * 2

    print(params)

    return params


def output_activation_0_order(pertinencies, value, params):

    num = 0
    den = 0

    for index,pertinency in enumerate(pertinencies):

        num += pertinency*params[index]*value
        den += pertinency

    return num/den