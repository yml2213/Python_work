import ast
import json

params = {
    'clientid': '1',
    'device_id': '0f1be1ff-44b7-47cb-afca-99a292820f03',
    'app_version': '1.7.2',
    'ip': '10.0.0.26',
    'system_name': 'android',
    'contentId': f'137505_111',
    'type': 'android',
    'modules': 'common:1',
    'creditType': 'SYS_READ',
    'siteid': '10001',
    'memberid': "137505",
    'memberId': "137505"
}
my_dict_json = json.dumps(params, sort_keys=True)
print(my_dict_json)

my_dict = ast.literal_eval(my_dict_json)
# print(type(my_dict))
