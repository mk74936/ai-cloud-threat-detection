import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        log = req.get_json()
        logging.info(f"Received log: {log}")

        if log.get("EventName") == "4625":
            return func.HttpResponse(json.dumps({
                "alert": True,
                "reason": "Failed login detected"
            }), status_code=200)

        return func.HttpResponse(json.dumps({"alert": False}), status_code=200)

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Error processing log", status_code=500)
