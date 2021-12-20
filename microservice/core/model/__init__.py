# TODO: En este paquete van los clases que representan los datos que va a
#       manejar el micro servicio. Pueden estar en este archivo o estar
#       ordenados en diferentes archivos dentro de este paquete.

"""Model."""

from datetime import datetime
from typing import Any, List
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from bson import ObjectId


@dataclass_json
@dataclass
class User:
    """User model."""

    email: str = None
    hashed_password: str = None
    is_active: bool = None

    def to_dict(self):
        return {
            "email": self.email,
            "is_active": self.is_active
        }

    def __repr__(self):
        return f"email=\"{self.email}\", " \
               f"is_active={self.is_active})>"


@dataclass_json
@dataclass
class InfluxData:
    """Influx data model."""

    measurement: str = None
    tags: dict = None
    fields: dict = None
    time: datetime = None


@dataclass_json
@dataclass
class FormulaMember:
    """Formula member data model."""

    tag: str = None
    indicator: ObjectId = None


@dataclass_json
@dataclass
class Action:
    """Action data model."""

    formula: str = None
    formula_members: list[FormulaMember] = None
    # prerequisites: list[ObjectId] = None


@dataclass_json
@dataclass
class QueryField:
    """QueryField data model."""

    name: str = None
    data_type: str = None
    field_type: str = None


@dataclass_json
@dataclass
class Query:
    """Query data model."""

    storage_query: str = None
    get_query: str = None
    fields: list[QueryField] = None
    source: ObjectId = None


@dataclass_json
@dataclass
class Source:
    """Source data model."""

    _id: ObjectId = None
    name: str = None
    connection_string: str = None
    credential: any = None


@dataclass_json
@dataclass
class Tag:
    """Tag data model."""

    name: str = None
    value: str = None


@dataclass_json
@dataclass
class Acl:
    """Acl data model."""

    user: str = None
    permission: str = None


@dataclass_json
@dataclass
class Metadata:
    """Metadata data model."""

    friendly_name: str = None    # nombre bonito para el usuario
    description: str = None
    module: str = None      # modulo ej bgp
    tags: List[Tag] = None
    acl: List[Acl] = None


@dataclass_json
@dataclass
class Indicator:
    """Indicator data model."""

    _id: ObjectId = None
    name: str = None
    measure: str = None
    unit: str = None
    type: str = None
    calculated: bool = None
    stored: bool = True
    query: Query = None
    action: Action = None
    metadata: Metadata = None


@dataclass_json
@dataclass
class ApiResponse:
    code: int = None
    type: str = None
    message: str = None


@dataclass_json
@dataclass
class Pagination:
    """General pagination."""

    items: int = None
    total_pages: int = None
    next_page: str = None
    actual_page: int = None
    previous_page: str = None
    data: Any = None


@dataclass_json
@dataclass
class Map:
    """Map data model."""

    script_field: str = None
    indicator_field: str = None
    type_field: str = None


@dataclass_json
@dataclass
class IndicatorToExtract:
    """Indicator to extract data model."""

    indicator: str = None
    fields: List[Map] = None


@dataclass_json
@dataclass
class ScriptAction:
    """Script action data model."""

    command_name: str = None
    specific_command_id: str = None
    indicators: List[IndicatorToExtract] = None


@dataclass_json
@dataclass
class StatScript:
    """Statistic scripts model."""

    _id: str = None
    name: str = None
    description:str = None
    actions: List[ScriptAction] = None


@dataclass_json
@dataclass
class Threshold:
    """Threshold model."""

    _id: ObjectId = None
    name: str = None
    kpi: ObjectId = None
    graphic: ObjectId = None
    limit = None
    comparator: str = None
    store: bool = None


@dataclass_json
@dataclass
class Graphic:
    """Graph model."""

    _id: ObjectId = None
    name: str = None
    icon: str = None
    kpi_list: List[ObjectId] = None
    grafana_iframe: str = None
    backend: str = None
    type: str = None


@dataclass_json
@dataclass
class CeleryId:
    """Celery model."""

    celery_job_id: ObjectId = None


@dataclass_json
@dataclass
class FieldsReport:
    """Field report data model."""

    field_name: str = None
    field_value: str = None


@dataclass_json
@dataclass
class IndicatorReport:
    """Indicator_field report data model."""

    indicator: ObjectId = None
    query: str = None
    fields: List[FieldsReport] = None
    credentials: str = None
    treshold: str = None


@dataclass_json
@dataclass
class ColumnsReport:
    """Columns report data model."""

    column_order: int = None
    column_name: str = None
    indicator: IndicatorReport = None


@dataclass_json
@dataclass
class MetadataReport:
    """Metadata report data model."""

    user_name: str = None
    description: str = None
    tenant: str = None
    tags: List[Tag] = None
    acl: List[Acl] = None


@dataclass_json
@dataclass
class Report:
    """Report data model."""

    _id: ObjectId = None
    name: str = None
    default_time_period: int = None
    key_field: str = None
    columns: List[ColumnsReport] = None
    metadata: MetadataReport = None
