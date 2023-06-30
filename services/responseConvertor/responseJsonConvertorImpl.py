from services.responseConvertor.responseJsonConvertor import ResponseJsonConvertor
import json

class ResponseJsonConvertorImpl(ResponseJsonConvertor):

    def resp_json_convertor(self, responseBody):
        try:
            responseJson = json.loads(responseBody)
            return responseJson
        except Exception as e:
            raise e