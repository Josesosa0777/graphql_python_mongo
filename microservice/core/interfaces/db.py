from abc import ABC, abstractmethod
from microservice.core.model import InfluxData, Indicator


class DBAdapter(ABC):
    """Clase adaptador de la base de datos.

    Esta clase debe reflejar todas las funcionalidades que va a
    proporcionar el adaptador de base de datos. Y la clase de
    implementación debe ser hija de esta.

    Cada funcionalidad que se escriba en el adaptador debe tener su
    contraparte en este archivo como un metodo abstracto.

    Por ejemplo si se necesita listar usuarios en esta clase debera
    existir un metodo abstracto que defina el nombre del metodo, sus
    parametros y el tipo de salida. Usuario debe ser una clase que
    represente los datos del usuario y que permita modelar los datos.

    @abstractmethod
    def listarUsuarios(query=None) -> List[Usuario]:
        pass
    """

    @abstractmethod
    def dummy(self):
        pass

    # @abstractmethod
    # def add_indicator(self, data: Indicator):
    #     """Insert a new Indicator."""
    #     pass

    # @abstractmethod
    # def get_total_indicators(self):
    #     """Get count of all indicators."""
    #     pass

    # @abstractmethod
    # def get_all_indicators(self, offset, limit):
    #     """Get all indicators with pagination."""
    #     pass

    # @abstractmethod
    # def get_indicator(self, id_indicator):
    #     """Get indicator by id."""
    #     pass

    # @abstractmethod
    # def update_indicator(self, id_indicator, new_indicator):
    #     """Update indicator by id."""
    #     pass

    # @abstractmethod
    # def delete_indicator(self, id_indicator):
    #     """Delete indicator by id."""
    #     pass

    # @abstractmethod
    # def add_stat_script(self, data):
    #     """Insert a new stat script."""
    #     pass

    # @abstractmethod
    # def get_total_stat_script(self):
    #     """Get count of all stat scripts."""
    #     pass

    # @abstractmethod
    # def get_all_stat_script(self, offset, limit):
    #     """Get count of all kpi's."""
    #     pass

    # @abstractmethod
    # def get_stat_script(self, id_stat_script):
    #     """Get stat script by id."""
    #     pass

    # @abstractmethod
    # def update_stat_script(self, id_stat_script, new_stat_script):
    #     """Update stat script by id."""
    #     pass

    # @abstractmethod
    # def delete_stat_script(self, id_stat_script):
    #     """Delete stat script by id."""
    #     pass

    # @abstractmethod
    # def get_command_from_stat_script(self, id_stat_script):
    #     """Get command by stat script id."""
    #     pass

    # @abstractmethod
    # def append_action_stat_script(self, id_script, action):
    #     """Append item action_Script by stat_Script id."""
    #     pass

    # @abstractmethod
    # def drop_action_stat_script(self, id_script, position):
    #     """Delete item action_Script by stat_Script id."""
    #     pass

    # @abstractmethod
    # def update_action_stat_script(self, id_script, position, new_data):
    #     """Update item action_Script by stat_Script id."""
    #     pass

    # @abstractmethod
    # def add_threshold(self, data):
    #     """Insert a new threshold."""
    #     pass

    # @abstractmethod
    # def get_total_threshold(self):
    #     """Get count of all threshold."""
    #     pass

    # @abstractmethod
    # def get_all_thresholds(self, offset, limit):
    #     """Get all thresholds."""
    #     pass

    # @abstractmethod
    # def get_threshold(self, id_threshold):
    #     """Get threshold by id."""
    #     pass

    # @abstractmethod
    # def update_threshold(self, id_threshold, new_threshold):
    #     """Update threshold by id."""
    #     pass

    # @abstractmethod
    # def delete_threshold(self, id_threshold):
    #     """Delete threshold by id."""
    #     pass

    # @abstractmethod
    # def add_graphic(self, data):
    #     """Insert a new graphic."""
    #     pass

    # @abstractmethod
    # def get_total_graphics(self):
    #     """Get count of all graphics."""
    #     pass

    # @abstractmethod
    # def get_all_graphics(self, offset, limit):
    #     """Get all graphics."""
    #     pass

    # @abstractmethod
    # def get_graphic(self, id_graphic):
    #     """Get graphic by id."""
    #     pass

    # @abstractmethod
    # def update_graphic(self, id_graphic, new_graphic):
    #     """Update graphic by id."""
    #     pass

    # @abstractmethod
    # def delete_graphic(self, id_graphic):
    #     """Delete graphic by id."""
    #     pass


class DBAdapterTimesSeries(ABC):
    """Interface for times series databases."""

    @abstractmethod
    def connect(self, connect_string):
        """Connect Time Series."""
        pass

    """
    @abstractmethod
    def save_kpi(self, timestamp, kpi, kpi_data):
        pass
    """

    @abstractmethod
    def save_measurement(self, data: InfluxData):
        """Save measurement."""
        pass

    @abstractmethod
    def get_measurement(self, measurement: str, start_time: str):
        """Get measurement."""
        pass

    @abstractmethod
    def save_measurement_batch(self, data: [InfluxData]):
        """Save measurement batch."""
        pass
