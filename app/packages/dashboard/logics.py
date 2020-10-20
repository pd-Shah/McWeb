import json
import clr
from settings import (
    PROXY_DLL,
    MISSION_TEMPLATE_DLL, 
    MTO_DLL_DIR,
)

clr.AddReference(PROXY_DLL)
clr.AddReference(MISSION_TEMPLATE_DLL)
clr.AddReference(MTO_DLL_DIR)

from flask import (
    flash,
    session,
)
from MissionTemplate import MissionTemplate
from MTO import MTO
from Proxy import (
    MissionTemplateProxy,
    SequenceDetailsProxy,
    TelecommandProxy,
    PUSServicesProxy,
)


def get_mission_list_api():
    objMissionTemplateProxy = MissionTemplateProxy()
    return objMissionTemplateProxy.GetMissionList(session['role_id'])


def get_telecommands_list_api(squence_id_list):
    result = {}
    seqdMng = SequenceDetailsProxy()
    for id in squence_id_list:
        tcList = seqdMng.GetTelecommands(id, session['role_id'])
        result[id] = tcList
    return result


def get_pus_services_list_api():
    pusMng = PUSServicesProxy()
    pusList = pusMng.GetPUSServiceList(session['role_id'])
    return pusList


def get_pus_telecommands_api(pusList):
    result = {}
    tcMng = TelecommandProxy()
    for pus in pusList:
        tcList = tcMng.GetPUSTelecommands(pus.PUSId, session['role_id'])
        result[pus.PUSId] = tcList
    return result


def create_mission_template(mission_name, description, Sequence_items):
    mission_template = MissionTemplate()
    template = json.loads(mission_template.GetInputFormat())
    Sequence_items = [item.strip() for item in Sequence_items]
    mission_name = mission_name.strip()
    description = description.strip()
    template["UserId"] = session['user_id']
    template["RoleId"] = session['role_id']
    template["username"] = session['username']
    template["MissionName"] = mission_name
    template["Description"] = description
    template["SequenceItems"].extend(Sequence_items)
    template = json.dumps(template)
    result = mission_template.InsertMissionTemplate(template)
    return json.loads(result)


def get_mto_data_source():
    mto = MTO()
    template = json.loads(mto.GetInputFormat())
    template["RoleId"] = session['role_id']
    template = json.dumps(template)
    result = mto.GetDataSource(template)
    return json.loads(result)