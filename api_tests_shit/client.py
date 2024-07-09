import os
import allure

from typing import Any

from dotenv import load_dotenv

load_dotenv()

URL: str = os.getenv('BASE_URL')


def attach_response(response: dict, name: str) -> allure:
    allure.attach(str(response), name=name, attachment_type=allure.attachment_type.JSON)


def attach_error(value: str, name: str) -> allure:
    allure.attach(value, name=name, attachment_type=allure.attachment_type.TEXT)


def allure_annotations(title, story, description, tag="",
                       severity=allure.severity_level.NORMAL, feature="REST-API") -> allure:
    def wrapper(func):
        func = allure.title(title)(func)
        func = allure.feature(feature)(func)
        func = allure.story(story)(func)
        func = allure.severity(severity)(func)
        func = allure.description(description)(func)
        func = allure.tag(tag)(func)
        return func

    return wrapper


def validate_response(self, response_json, response_type, schema) -> Any:
    if 'error' in response_json:
        attach_error(str(response_json), name="Invalid Response")
        assert False, "Response does not contain necessary fields"
    else:
        try:
            attach_response(response_json, response_type)
            valid_response = schema(**response_json)
            if response_type == "Response":
                self.valid_response = valid_response
                return self.valid_response
            elif response_type == "Delete Response":
                self.valid_delete_response = valid_response
                return self.valid_delete_response
        except Exception as e:
            attach_error(str(e), name="Validation Error")
            assert False, f"Validation error: {str(e)}"
