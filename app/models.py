from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute, BooleanAttribute

from configs import REGION, HEXA_SLEEP_RESULT_TABLE

class HexaSleepResultModel(Model):

    class Meta:
        table_name = HEXA_SLEEP_RESULT_TABLE
        region = REGION

    room_id = UnicodeAttribute(hash_key=True)
    start_timestamp = UnicodeAttribute(range_key=True)
    end_timestamp = UnicodeAttribute(null=True)
    last_seq_num = NumberAttribute(null=True)
    

if __name__ == "__main__":
    hsrm = HexaSleepResultModel()
    hsrm.create_table(read_capacity_units=10, write_capacity_units=1, wait=True)