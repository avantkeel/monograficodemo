from utils.adapters.httpAdapter import Request, Response

def HealthHandler(req: Request, res: Response):
    res.json({"status": "Ok"}, status=200)
