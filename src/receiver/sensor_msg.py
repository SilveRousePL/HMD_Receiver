import json

# {"sensor_id": %u, "time": "%u", "type": "%s", "uptime": %u, "motion": %d, "motion_counter": %u, "temp0": %f}
class SensorMsg:
    def __init__(self, dict):
        vars(self).update(dict)
    
    @staticmethod
    def get_obj(json_string):
        return json.loads(json_string, object_hook=SensorMsg)
