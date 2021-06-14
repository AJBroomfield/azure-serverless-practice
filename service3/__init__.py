import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    letters='abcdefghijklmnopqrstuvwxyz'
    let_code=""
    for _ in range(5):
        letter = random.choice(letters)
        rand = random.choice([True, False])
        if rand == True:
            letter = letter.upper()
        let_code += letter
    
    return func.HttpResponse(f"{let_code}")

