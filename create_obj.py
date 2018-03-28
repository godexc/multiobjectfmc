import json
import sys
import requests


username = "admin"
if len(sys.argv) > 1:
    username = sys.argv[1]
password = "sf"
if len(sys.argv) > 2:
    password = sys.argv[2]
server = "https://fmcrestapisandbox.cisco.com"
if len(sys.argv) > 3:
    server = sys.argv[3]

r = None
headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = server + api_auth_path
try:
    r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username, password),
                      verify=False)
    auth_headers = r.headers
    auth_token = auth_headers.get('X-auth-access-token', default=None)
    if auth_token == None:
        print("auth_token not found. Exiting...")
        sys.exit()
except Exception as err:
    print("Error in generating auth token --> " + str(err))
    sys.exit()

headers['X-auth-access-token'] = auth_token

api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"  # param
url = server + api_path
if (url[-1] == '/'):
    url = url[:-1]

# POST OPERATION

with open("host_objects.txt", "rb") as fin:
    content = json.load(fin)

for post_data in content:

   try:
       r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
       status_code = r.status_code
       resp = r.text
       print("Status code is: " + str(status_code))
       if status_code == 201 or status_code == 202:
           print("Post was successful...")
           json_resp = json.loads(resp)
           print(json.dumps(json_resp, sort_keys=True, indent=4, separators=(',', ': ')))
       else:
           r.raise_for_status()
           print("Error occurred in POST --> " + resp)
   except requests.exceptions.HTTPError as err:
       print("Error in connection --> " + str(err))
   finally:
       if r: r.close()
