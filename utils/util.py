def respOutCustom(statusCode:str, message:str, data: None)->dict[str, any]:
    resp = {
        "statusCode": statusCode,
        "message": message,
        "data":data
    }
    return resp