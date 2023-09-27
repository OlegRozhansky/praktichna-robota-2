import json
import random

def lambda_handler(event, context):
    # TODO implement
    rnd = random.randint(1, 6)
    return rnd
    
