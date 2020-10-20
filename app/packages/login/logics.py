import clr
from settings import PROXY_DLL
clr.AddReference(PROXY_DLL)
from Proxy import LoginProxy
from flask import (
    flash,
)

# "test", "1", "PARS1_FM", "pedram", "Tehran"
def call_login_api(
    username,
    satellite_name,
    server_name,
    ground_station_name,
    password, ):
    objLoginProxy = LoginProxy()
    result = objLoginProxy.CheckLogin(
        username,
        password, 
        satellite_name,
        server_name,
        ground_station_name, )
    if result is not None:
        return {'user_id': result.UserId, 'role_id': result.RoleId, "username": username,}
    else:
        return None
