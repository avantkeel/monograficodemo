from utils.adapters.httpAdapter import Request, Response

def HelloHandler(req: Request, res: Response):
    res.json({"message": "Hello, user"}, status=200)
