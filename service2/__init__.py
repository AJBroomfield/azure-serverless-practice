import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(f"{random.randint(10000,99999)}")
